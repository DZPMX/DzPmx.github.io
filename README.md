# DzPmx.github.io

使用 GitHub Pages、Jekyll 和自定义布局样式的个人博客源文件。

博客地址：<https://dzpmx.github.io/>。

## 发布设置

1. 打开仓库 **Settings → Pages**。
2. 将 **Source** 设为 **Deploy from a branch**，分支选择 **main**，目录选择 **/ (root)**，保存。
3. 在仓库 **Actions** 页面检查部署结果，成功后访问博客地址。

## 写文章

在 `_posts` 中添加 `YYYY-MM-DD-文章名称.md`。日期填写实际发布日期，文件顶部保留文章信息：

```markdown
---
layout: post
title: "文章标题"
date: 2026-10-05 00:00:00 +0800
---

正文使用 Markdown 编写。
```

修改提交到 `main` 后，由 GitHub Pages 自动生成和发布。

## 修改首页和名称

- `index.md`：首页欢迎文字；文章列表由首页布局自动生成。
- `_config.yml`：博客标题、介绍、GitHub 用户名、语言和时区。
- `_layouts/`：公共页面、首页和文章页布局。
- `assets/css/site.css`：配色、排版、代码高亮和手机布局。
- `_posts/2026-10-05-getting-started.md`：入门文章，可以编辑或删除。

本仓库通过 GitHub Pages 自带的 Jekyll 环境发布，不需要在本地安装 Ruby 或 Node.js。
