# DZPMX Blog

个人博客：<https://dzpmx.github.io/>。使用 GitHub Pages、Jekyll 和 [Hux Blog](https://github.com/Huxpro/huxpro.github.io) 主题。

## 写文章

在 `_posts` 中添加 `YYYY-MM-DD-文章名称.md`，或直接编辑对应的 Markdown。上传到 `main` 后，GitHub Pages 会自动发布；到仓库 **Actions** 查看部署是否成功。只有仓库文件保存成功还不代表网页已经更新。

```yaml
---
layout: post
title: "文章标题"
date: 2026-10-07 00:00:00 +0800
header-img: "assets/images/文章目录/cover.jpg"
no-catalog: false
typora-root-url: ../
typora-copy-images-to: ../assets/images/文章目录
tags:
  - Graphics Sutdy
---
```

正文使用 Markdown。用 `##`、`###` 等标题组织章节，CATALOG 会读取正文标题生成跳转；没有小标题的短文设置 `no-catalog: true`，不要为凑目录改动正文。本站当前 Hux 模板读取的是 `no-catalog`，不使用旧文档中的 `catalog` 字段。

图片放在 `assets/images/`，正文引用例如：

```markdown
![图片说明](/assets/images/文章目录/figure-01.png)
```

图片需要图注时，可以沿用现有文章的 `<figure>` / `<figcaption>` 结构。正文图片保留比例，居中并限制显示宽度。文章日期决定首页顺序，日期新的在前；文件名和 `date` 保持一致。

当前标签为 `Technical Artist`、`Graphics Sutdy` 和 `闲谈`。标签写在文章开头的 `tags` 数组中，文章头部、FEATURED TAGS 和 Archive 会共同读取，不需要手工编辑标签列表。含空格的标签保持为一个列表项。

## 本地写作

本地仓库位于 `E:\GitHub\DzPmx.github.io`。用 Typora 打开这个文件夹，在 `_posts` 中编辑文章；保留开头的日期、头图、Tag 和目录设置。新文章复制上面的配置，将文章目录、标题、日期和头图替换为实际值。

- 开始编辑前，在 GitHub Desktop 中点击 **Fetch origin**，有更新时再点击 **Pull origin**。
- `typora-root-url: ../` 让 Typora 从博客根目录查找 `/assets/images/...` 图片；`typora-copy-images-to` 指定这篇文章插入图片时的保存目录。
- 插入或粘贴图片后，检查图片链接以 `/assets/images/` 开头。不要提交 `C:\...`、`file:///...` 或 `../assets/...` 这样的正文图片地址；文章发布后的网址层级与本地文件夹不同。
- Typora 中保存文件后，在 GitHub Desktop 查看文章和图片改动，填写提交说明，点击 **Commit to main**，再点击 **Push origin**。只有推送后才会触发博客发布。
- Typora 用于正文编辑，头图、CATALOG 和 Hux 页面布局以实际博客页面为准；不需要导出 HTML 或插入 `[TOC]`。

## 站点维护

- `_config.yml`：博客名称、作者、默认头图、语言和时区。
- `index.md`：首页欢迎文字。
- `_layouts/`、`_includes/`：Hux 页面结构及本站集成。
- `css/bootstrap.min.css`、`css/hux-blog.css`：Hux 使用的原版样式。
- `css/dzpmx.css`：本站图片排版和现有社交图标样式。
- `js/`：Hux 导航、目录和标签归档依赖。
- `assets/images/blog-cover.jpg`：首页、START 和 Archive 的山景头图。

**Settings → Pages** 使用 **Deploy from a branch → main → / (root)**。不需要在本地安装 Ruby、Node.js 或运行构建命令。
