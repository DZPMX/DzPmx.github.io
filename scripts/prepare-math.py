"""Prepare math-enabled posts in the Actions checkout before Jekyll runs."""

from pathlib import Path
import re
import subprocess

import yaml


FRONT_MATTER = re.compile(
    r"\A(?P<header>---\n(?P<metadata>.*?)\n---\n)(?P<body>.*)\Z", re.DOTALL
)


def prepare_math_posts():
    posts_directory = Path(__file__).resolve().parents[1] / "_posts"
    for source_path in sorted(posts_directory.glob("*.md")):
        document = FRONT_MATTER.match(source_path.read_text(encoding="utf-8"))
        if document is None:
            continue
        metadata = yaml.safe_load(document["metadata"]) or {}
        if metadata.get("math") is not True:
            continue

        # Pandoc protects TeX before Markdown can treat pipes or escapes as markup.
        rendered = subprocess.run(
            [
                "pandoc",
                "--from=markdown+tex_math_dollars-smart",
                "--to=html5",
                "--mathjax",
                "--wrap=none",
                "--no-highlight",
            ],
            input=document["body"],
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=True,
        )
        # Only this disposable Actions checkout is changed; authored Markdown stays in Git.
        source_path.with_suffix(".html").write_text(
            document["header"] + rendered.stdout, encoding="utf-8"
        )
        source_path.unlink()
        print(f"Prepared math article: {source_path.name}")


if __name__ == "__main__":
    prepare_math_posts()
