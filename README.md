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
- `assets/css/site.css`：封面、导航、双栏文章列表、正文排版和手机布局。
- `assets/images/blog-cover.jpg`：首页和文章页共用的封面图；替换图片即可更新封面。
- `_posts/2026-10-05-getting-started.md`：入门文章，可以编辑或删除。

本仓库通过 GitHub Pages 自带的 Jekyll 环境发布，不需要在本地安装 Ruby 或 Node.js。

## 视觉设计

页面以 Candycat Blog（<https://candycat1992.github.io/>）的字体回退顺序、字号、字重、颜色、间距和响应式断点为对照，使用 Jekyll 模板与 CSS 实现。界面栏目使用英文，文章保持原文；日期采用 `Posted by 作者 on Month D, YYYY` 格式。侧栏头像直接使用 `_config.yml` 中 GitHub 用户名对应的公开头像。

正文使用参考站的系统字体栈，日期使用 Lora／Times New Roman，代码使用 Fira Code／Menlo／Monaco／Consolas 的回退顺序；未额外下载字体，实际字体取决于设备已有字体。代码配色对齐参考站的 One Dark 规则。页面宽度与断点采用参考站的 750／970／1170px 和 768／992／1200px。

手机导航使用原生折叠菜单承载现有链接；没有移植参考站的搜索、评论、作品集及桌面滚动导航脚本。原创封面和现有文章继续保留。

封面由内置 imagegen 工具生成。提示词：

> Use case: photorealistic-natural. Asset type: full-width personal blog header photograph. Create an original panoramic editorial landscape photograph for a professional Chinese personal blog. Layered forested mountains at blue hour, a calm lake low in the frame, soft mist between ridgelines, restrained charcoal and slate-blue tones, a faint warm glow near the horizon. Natural photographic detail, peaceful and understated. Ultra-wide horizontal composition, approximately 3:1. Keep the central upper-middle area dark and visually quiet so large white website title text can be overlaid in HTML; edge-to-edge landscape without borders. No people, buildings, logos, symbols, text, UI or watermark.
