---
layout: post
title: "Uncharted4中布料与头发的美术和渲染流程"
date: 2026-10-07 00:00:00 +0800
header-img: "assets/images/uncharted-4-cloth-and-hair/siggraph-cover.jpg"
header-mask: 0.35
header-img-credit: "Yibing Jiang / Naughty Dog, SIGGRAPH 2016"
header-img-credit-href: "https://advances.realtimerendering.com/s2016/"
no-catalog: false
tags:
  - Graphics Sutdy
typora-root-url: ../
typora-copy-images-to: ../assets/images/uncharted-4-cloth-and-hair
---

本文是 SIGGRAPH 2016 演讲《The Process of Creating Volumetric-based Materials in Uncharted 4》的 PPT 笔记，主要记录布料与头发的美术和渲染流程。该分享包含以下四个章节：

1. 角色 Shading 管线（背景介绍）
2. 布料材质库
3. 头发材质库
4. 着色器包的介绍和实例

本文只详细介绍第二节和第三节。对其他部分感兴趣的话，可以下载原 PPT 查看。

原 PPT 的下载链接：

<p>
  <a href="https://link.zhihu.com/?target=https%3A//advances.realtimerendering.com/s2016/">
    Advances in Real-Time Rendering- SIGGRAPH 2016 advances.realtimerendering.com/s2016/
  </a>
</p>
## 1. 布料材质库
在制作衣服材质时，顽皮狗的开发者遇到了以下挑战：

1. 布料的种类特别多
2. 怎么实现不同布料的反射模型
3. 布料具有较高的散射特性
4. 可平铺的微观编织结构
5. 具有体积感的自阴影
6. 具有一定的细节瑕疵，使得外观更真实

### 微观编织结构
针对微观编织结构，开发者选择了一些不同的图案，并在 Maya 中为其建模。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-01.png" alt="微观编织结构的图案" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>微观编织结构的图案</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-02.png" alt="在 Maya 中对编织图案建模" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>在 Maya 中对编织图案建模</figcaption>
</figure>

建模时，先制作图案中的单个元素，再复制模型，最后使用脚本将模型合并。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-03.png" alt="制作图案元素，平铺（Tiling）后合并" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>制作图案元素，平铺（Tiling）后合并</figcaption>
</figure>
之所以不使用扫描的织物资产，一方面是为了节省纹理内存：这种可平铺的微观编织结构只需要 64\*64 的贴图。另一方面，这样可以保留微观编织结构的细节，即使使用 MipMap，也不会模糊得看不清。

在 Uncharted 4 中，一共实现了 12 种不同的微观编织结构纹理、4 种不同的瑕疵细节纹理，以及 2 种布料褶皱和做旧的方法。通过调节各类细节的尺寸并进行组合，就能表现出大多数织物在现实中的外观，而不必对每种布料都进行扫描。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-04.png" alt="只需 64×64 的纹理，即可平铺" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>只需 64×64 的纹理，即可平铺</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-05.png" alt="细节占比高，不会因 MipMap 而丢失细节" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>细节占比高，不会因 MipMap 而丢失细节</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-06.png" alt="组合不同种类的纹理，实现大多数织物的效果" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>组合不同种类的纹理，实现大多数织物的效果</figcaption>
</figure>

以下是 Uncharted 4 中叠加多种不同分辨率的可平铺细节后的材质预览。从基础的布料 BRDF 开始，先添加微观编织结构贴图，再添加织物老化、瑕疵和褶皱细节，最终呈现出非常真实的效果。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-07.png" alt="织物材质的细节叠加" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>织物材质的细节叠加</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-08.png" alt="织物材质的细节叠加" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>织物材质的细节叠加</figcaption>
</figure>

此外，衣服上的缝线和孔洞还使用了 2U 来添加，思路与布料编织图案的制作相同。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-09.png" alt="添加布料的缝线和孔洞" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>添加布料的缝线和孔洞</figcaption>
</figure>

### 布料的反射模型
对于丝绸、丝绒和其他高反射的织物，开发者尝试了 GGX 各向异性和 Kajiya-Kay 两种模型。GGX 各向异性版本的效果稍好，但在 Uncharted 4 的光照模型下，大多数情况下很难看出优势，因此最终选择了性价比更高的 Kajiya-Kay 版本。

对于棉布、羊毛等布料，开发者采用了 Ready at Dawn 工作室的布料反射模型，并对散射效果进行了调整。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-10.png" alt="开销更低的布料散射效果" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>开销更低的布料散射效果</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-11.png" alt="修改 Shading 后，布料的散射效果更明显，外观也更柔软" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>修改 Shading 后，布料的散射效果更明显，外观也更柔软</figcaption>
</figure>

## 2. 头发材质库
发丝非常细，并且具有半透明性。每根发丝的法线不同，发丝之间也会产生自阴影。为了让头发更有体积感，需要逐一解决这些问题。

虽然 PS4 的性能有大幅提升，但仍然不足以实时渲染上百万根发丝。由于研发时间有限，开发者也没有对曲面细分着色器进行深入研究，最终还是选择使用发片（Hair Cards）来制作头发。

完全使用 AlphaBlend 渲染头发虽然能获得很好的效果，但会带来严重的 OverDraw。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-12.png" alt="完全使用 Alpha Blend 会产生大量 OverDraw" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>完全使用 Alpha Blend 会产生大量 OverDraw</figcaption>
</figure>

因此，游戏中绝大部分头发都使用 Dither Alpha，并配合 TAA。这会导致人物快速移动时出现拖影。为避免这一问题，开发者调高了头发的裁剪阈值，让发丝不再那么细薄。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-13.png" alt="使用 Dither Alpha 配合 TAA 会出现拖影" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>使用 Dither Alpha 配合 TAA 会出现拖影</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-14.png" alt="调高裁剪阈值，让发丝更粗，以适配 Dither 和 TAA" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>调高裁剪阈值，让发丝更粗，以适配 Dither 和 TAA</figcaption>
</figure>

但调高阈值后，又会出现另一个问题：头发看起来会有“发片感”。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-15.png" alt="头发有发片感" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>头发有发片感</figcaption>
</figure>

开发者总结了导致“发片感”的一些原因。首先，Hair Cards 使用的是顶点法线，而不是单根发丝的法线。

其次，锐利的太阳光阴影让头发看起来像一个不透明的物体，但发丝实际上具有半透明性。

### 头发处理
为解决上述问题，3D 艺术家在摆放发片时，会让它们相互交错，使头发更有体积感。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-16.png" alt="体块处理" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>体块处理</figcaption>
</figure>

为了让发片之间平滑过渡，开发者统一了发片的顶点法线（看起来像是将法线映射到球面或 Mesh 体块上的效果）。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-17.png" alt="统一法线" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>统一法线</figcaption>
</figure>
此外，还烘焙了变化图，用来打散高光和逆光散射，让发丝感更突出。

<img src="/assets/images/uncharted-4-cloth-and-hair/image-20261008023014465.png" alt="image-20261008023014465" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">

### 头发阴影

在头发阴影方面，如果减少阴影，会让头发看起来过于平坦，不够立体。

开发者尝试使用一组呈球形覆盖头模的灯光，预计算头发的阴影，并将其烘焙到贴图中。这种阴影与方向光无关（此前曾尝试烘焙多组不同方向光的信息，后来放弃了这一方案，只使用 LocalLight 烘焙出类似 AO 效果的阴影）。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-18.png" alt="使用呈球形覆盖的灯光，烘焙阴影" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>使用呈球形覆盖的灯光，烘焙阴影</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-19.png" alt="Bake Shadow" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>Bake Shadow</figcaption>
</figure>

Bake Shadow 让头发看起来更有深度感和体积感。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-20.png" alt="更好的头发质感" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>更好的头发质感</figcaption>
</figure>

头发阴影使用了两张贴图：一张 1K 贴图提供所有发片共享的细节；另一张 512 的贴图存储烘焙阴影，为不同发片提供各自的细节。烘焙阴影使用 UV2 存储信息。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-21.png" alt="两张细节纹理" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>两张细节纹理</figcaption>
</figure>

如果只是把游戏内阴影与烘焙阴影直接相乘，结果就会显得非常扁平。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-22.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

针对这个问题，需要减少游戏中头发的硬阴影。直接对 Shadow 做 Blur 非常耗费性能。此前，开发者调高了头发的裁剪阈值，让发丝更粗；而在头发的 Shadow Pass 中，可以重置裁剪阈值，让这一阶段的发丝更细，从而使阴影更加柔和。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-23.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

为使头发的渲染更真实，开发者还对 Shading 做了以下调整：

1. 为 BakeShadow 添加 Light Wrap
2. 使用光照探针的强度和头发的颜色来控制 BakeShadow

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-24.png" alt="修改 Shadow 的 Shading 计算" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>修改 Shadow 的 Shading 计算</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-25.png" alt="添加 Bake Shadow 前后" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>添加 Bake Shadow 前后</figcaption>
</figure>

### 头发的散射
头发散射主要包含两个关键部分：发丝之间的散射和背光散射。发丝间的散射采用了类似布料散射的方法，能呈现出较好的效果。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-26.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

对于背光散射，可以将头发看作一个球体。其散射表现主要与灯光、相机角度和表面法线相关，散射强度随头发颜色、形状、长度和光照强度而变化。以下是《神秘海域 4》的散射 Shading 计算，以及游戏中使用的参数参考值。ScatterPower 是一个幂参数，用于调整散射的菲涅耳形状。在《神秘海域 4》中，短发的取值为 11，长发则为 9。

lightScale 的取值根据头发的散射值确定。对于大多数金发，开发者会选择更高的值。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-27.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

### 头发着色模型
头发着色采用标准的 Kajiya-Kay 模型。

为了增加高光的变化，所有材质球都会使用一张可平铺的 specular variation mask。高光扰动能让玩家感受到发丝细节，发片的 UV 布局也保持统一。虽然该 Mask 不能完全匹配所有发丝的走向，但由此产生的问题并不明显，对于 NPC 和多人游戏角色来说，效果已经足够好了。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-28.png" alt="Kajiya Shading 和 Specular Variation Mask" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>Kajiya Shading 和 Specular Variation Mask</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-29.png" alt="错误并不明显" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>错误并不明显</figcaption>
</figure>

---
