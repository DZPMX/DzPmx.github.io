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

本文为SIGGRAPH2016《The Process of Creating Volumetric-based Materials in Uncharted 4》的PPT的笔记，内容上分为布料和头发两个部分的美术和渲染流程。分享主要包含了以下四个章节内容

1. 角色Shading管线（背景介绍）
2. 布料材质库
3. 头发材质库
4. 着色器包的介绍和实例

这里只会对第二节和第三节的内容进行详细的阐述，其它部分如感兴趣可以自行下载原PPT观看

原PPT的下载链接：

<p>
  <a href="https://link.zhihu.com/?target=https%3A//advances.realtimerendering.com/s2016/">
    Advances in Real-Time Rendering- SIGGRAPH 2016 advances.realtimerendering.com/s2016/
  </a>
</p>
## 1.布料材质库
在制作衣服材质方面方面，顽皮狗的开发者遇到了一下的挑战：

1. 布料的种类特别多
2. 怎么实现不同布料的反射模型
3. 布料具有较高的散射特性
4. 可平铺的围观的编织结构
5. 具有体积感的自阴影
6. 具有一定的细节瑕疵，使得外观更真实

### 微观编制结构
针对微编织结构，开发者们选择了一些不同的图案，将其在Maya中建模

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-01.png" alt="微编织结构的图案" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>微编织结构的图案</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-02.png" alt="Maya中对编织图案建模" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>Maya中对编织图案建模</figcaption>
</figure>

在对其进行建模的过程中，会先以图案的单个元素形状进行制作，然后复制模型，使用脚本对模型进行合并

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-03.png" alt="制作图案元素，Tilling后合并" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>制作图案元素，Tilling后合并</figcaption>
</figure>
对于为什么不使用扫描的织物资产，一方面是为了节省纹理的内存，这种具有tilling性质的微观编制结构只需要64\*64的贴图大小，另一方面，这样可以保留微编织结构的细节，即使被MipMap也不会糊的看不清。

在Uncharted4中，一共实现了12种不同的微观编织结构纹理，4种不同的瑕疵细节纹理，2种布料褶皱和做旧的方法。结合每种细节可调节的尺寸做各种组合，实现了大多数织物布料在现实的效果，而不必每种都使用扫描的办法。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-04.png" alt="只需要64*64的大小，即可Tilling" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>只需要64*64的大小，即可Tilling</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-05.png" alt="细节占比高，不会因为MipMap导致细节丢失" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>细节占比高，不会因为MipMap导致细节丢失</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-06.png" alt="不同纹理种类的组合以实现大多数织物的效果" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>不同纹理种类的组合以实现大多数织物的效果</figcaption>
</figure>

以下是Uncharted4中多种不同分辨率的可平铺细节叠加的材质预览效果，从基础的布料BRDF，添加微观编织结构贴图，再添加织物老化和缺陷细节以及褶皱后效果非常的真实。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-07.png" alt="织物材质的细节叠加" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>织物材质的细节叠加</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-08.png" alt="织物材质的细节叠加" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>织物材质的细节叠加</figcaption>
</figure>

除此之外，对于实际的衣服部分还使用了2U去添加布料的缝线和孔洞，实际思路和布料的编织图案相同。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-09.png" alt="添加布料的缝线和孔洞" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>添加布料的缝线和孔洞</figcaption>
</figure>

### 布料的反射模型
对于丝绸，丝绒和其它高反射的织物布料，开发者同时尝试了GGX各向异性和Kajiya-Kay两种模型。GGX各向异性版本的效果要稍好，不过在Uncharted4的光照模型下，大多数情况下比较难看出优势，所以其选择了更性价比更好的Kajiya-Kay的版本。

对于棉布，羊毛等布料，我们用了Ready at Dawn’s 工作室的布料反射模型并做了散射效果上的修改

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-10.png" alt="更廉价布料散射效果" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>更廉价布料散射效果</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-11.png" alt="在修改Shading后，布料会看起来比之前有更多的散射，更柔软" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>在修改Shading后，布料会看起来比之前有更多的散射，更柔软</figcaption>
</figure>

## 2.头发材质库
发丝具有非常细且半透的特性，每根发丝法线不同，发丝之间相互自阴影。为了使头发更有体积感，需要逐一去解决一些问题。

PS4在性能上虽然有大幅度的提升，但是仍然不足达到实时渲染上百万根发丝的效果，因为有限的研发时间，也没有在曲面细分着色器上研究太深，最终还是考虑使用发片（Hair Cards）的方式来制作头发

完全使用AlphaBlend渲染头发虽然会有一个非常好的效果，但会带来非常严重的OverDraw情况。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-12.png" alt="完全使用Alpha Blend会有大量的OverDraw" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>完全使用Alpha Blend会有大量的OverDraw</figcaption>
</figure>

因此对于绝大部分的头发，在游戏中都是使用Dither Alpha并配合TAA。这会导致人物快速移动时有拖影的效果，为了避免这样的问题，开发者调整高了头发的裁剪阈值，使得头发的发丝本身不那么薄和细。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-13.png" alt="使用Dither Alpha配合TAA会有拖影的情况" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>使用Dither Alpha配合TAA会有拖影的情况</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-14.png" alt="调高裁剪阈值，使得头发更粗来适配Dither和TAA" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>调高裁剪阈值，使得头发更粗来适配Dither和TAA</figcaption>
</figure>

但调高阈值后，会导致另外一个问题，头发看起来会有“发片感”。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-15.png" alt="头发有发片感" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>头发有发片感</figcaption>
</figure>

对于这个问题，开发者总结了一些导致发片感的原因，首先Hair Cards使用了顶点法线，而不是单独的发丝法线，

其次，锐利的太阳光阴影使得头发看起来是一个不透明的物体，但是发丝其实是半透的。

### 头发处理
基于以上的问题，3D艺术家在处理头发发片时，摆放的过程中，会相互交错让其更有体积感

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-16.png" alt="体块处理" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>体块处理</figcaption>
</figure>

为了让发片之间平滑过渡，统一了发片的顶点法线（看起来像是对法线做了球面或者Mesh体块的映射效果）。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-17.png" alt="统一法线" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>统一法线</figcaption>
</figure>
此外还烘焙了变化图，用其打散高光和逆光散射，使得发丝感、更突出

<img src="/assets/images/uncharted-4-cloth-and-hair/image-20261008023014465.png" alt="image-20261008023014465" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">

### 头发阴影

在头发阴影层面，如果减少阴影，会使得头发看起来太平面，不够立体。

开发者尝试了使用一组球形覆盖头模的灯光，来预计算头发的阴影，Bake到贴图中，该阴影是与方向光无关的的阴影（之前有尝试Bake多组不同方向光的信息，后来放弃未采用，只用LocalLight来烘培一个类似AO效果的阴影）

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-18.png" alt="球型覆盖灯光，烘培阴影" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>球型覆盖灯光，烘培阴影</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-19.png" alt="Bake Shadow" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>Bake Shadow</figcaption>
</figure>

Bake Shadow使得头发看起来更有深度感，有体积感。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-20.png" alt="更好的头发质感" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>更好的头发质感</figcaption>
</figure>

在头发阴影这里使用了两张贴图，一张1k贴图给所有发片共享细节，一张512的贴图用来存储Bake阴影，给到每个不同的发片不同的细节，Bake阴影使用UV2来存储信息。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-21.png" alt="两张细节纹理" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>两张细节纹理</figcaption>
</figure>

如果只是把游戏内阴影与烘焙阴影直接相乘，结果就会显得非常扁平。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-22.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

针对这个问题，需要减少在游戏中头发出现的硬阴影。对shadow做blur其实特别耗费性能。在之前对发丝的处理中，我们调高了头发的裁剪阈值，使得发丝更粗，而对头发的Shadow则可以使头发shadowpass的裁剪阈值重置，使得Shadowpass的头发更细，这样Shadow就会更加柔和。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-23.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

这里对头发的shading做了一些调整，来使得头发的渲染更真实，

1. 对BakeShadow添加了Light Wrap
2. 使用光照探针的强度和头发的颜色来控制BakeShadow

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-24.png" alt="修改Shadow的Shading计算" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>修改Shadow的Shading计算</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-25.png" alt="添加Bake Shadow前后" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>添加Bake Shadow前后</figcaption>
</figure>

### 头发的散射
对于头发散射的两个关键元素，主要是发丝之间的散射和背光的散射效果。发丝间的散射使用了类似布料散射的Trick，能呈现较好的效果

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-26.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

对于背光散射，可以将头发考虑成一个球体，其散射表现主要和灯光，相机角度，表面法线相关，散射的强度根据头发颜色、头发形状、头发长度和光照强度而变化。以下是神秘海域4给到的散射Shading计算，并给出的他们游戏中参数的参考值。 ScatterPower是一个幂参数，用于调整散射的菲尼尔形状，对于短发，在神秘海域4中是11，长发则为9。

lightScale 是我们根据头发的散射值选择的值。对于大多数金发，我们选择更高的值。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-27.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

### 头发着色模型
在着色模型的选择上是标准的Kajiya-Kay。

在高光的变化上，所有的材质球都会用一张可以平铺的specualr vairation mask，因为高光扰动会给玩家发丝的感觉，且发片 UV 布局统一。最后虽然该Mask并不能匹配所有的头发走向，但是这块产生的问题并不明显，对于 NPC 和多人游戏角色来说已经足够好了。

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-28.png" alt="KajiyaShading和Specualr Vairation Mask" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>KajiyaShading和Specualr Vairation Mask</figcaption>
</figure>

<figure>
  <img src="/assets/images/uncharted-4-cloth-and-hair/figure-29.png" alt="错误并不明显" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
  <figcaption>错误并不明显</figcaption>
</figure>

---
