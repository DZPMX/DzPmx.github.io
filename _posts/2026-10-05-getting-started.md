---
layout: post
title: "博客使用指南：发布第一篇文章"
date: 2026-10-05 00:00:00 +0800
---

这篇入门文章介绍如何更新这个博客。博客使用 GitHub Pages、Jekyll 和 Minima 主题，文章以 Markdown 文件保存。

## 发布新文章

1. 打开 [博客仓库](https://github.com/DzPmx/DzPmx.github.io)。
2. 进入 `_posts` 文件夹，选择 **Add file → Create new file**。
3. 按照 `YYYY-MM-DD-文章名称.md` 的格式填写文件名，例如 `2026-10-05-my-first-post.md`。
4. 参考下面的模板填写文章，把日期和标题改成实际内容。
5. 将修改提交到 `main` 分支。Pages 配置完成后，GitHub 会自动生成并更新网站。

```markdown
---
layout: post
title: "我的第一篇文章"
date: 2026-10-05 00:00:00 +0800
---

这里是正文。

## 一个小标题

继续写下你的内容。
```

## 修改或删除这篇入门文章

在仓库中打开 `_posts/2026-10-05-getting-started.md`，即可修改本文；不再需要时可以删除这个文件。

## 参考

- [GitHub Pages 内容发布说明](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/adding-content-to-your-github-pages-site-using-jekyll)
- [Minima 主题](https://github.com/jekyll/minima)
