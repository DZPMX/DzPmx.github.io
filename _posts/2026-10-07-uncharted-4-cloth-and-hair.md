---
layout: post
title: "神秘海域4的布料与头发流程"
date: 2026-10-07 00:00:00 +0800
---

本文为[SIGGRAPH2016](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=SIGGRAPH2016&zhida_source=entity)《The Process of Creating Volumetric-based Materials in Uncharted 4》的PPT的笔记，内容上总体分为布料纤维和头发两个部分的美术和渲染流程。至于为什么会有这篇文章，是因为面试时被问到了，而且头发部分的美术流程现在应用的也比较广泛，看了一遍怕记不住，索性就当记个笔记，顺带分享给有兴趣的人也一起看看。如果有描述错误的地方可以评论我会及时更正，感谢！

分享主要包含了四个部分的内容

1. 早期状态建立角色[Shading管线](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=Shading%E7%AE%A1%E7%BA%BF&zhida_source=entity)（背景介绍）
2. 建立[织物着色器库](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=%E7%BB%87%E7%89%A9%E7%9D%80%E8%89%B2%E5%99%A8%E5%BA%93&zhida_source=entity)
3. 建立[头发着色器库](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=%E5%A4%B4%E5%8F%91%E7%9D%80%E8%89%B2%E5%99%A8%E5%BA%93&zhida_source=entity)
4. 着色器包的介绍和实例

这里只会对第二个部分和第三个部分的内容进行详细的阐述，其它部分如感兴趣可以自行下载原PPT观看

原PPT的下载链接：

<p>
  <a href="https://link.zhihu.com/?target=https%3A//advances.realtimerendering.com/s2016/">
    <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/siggraph-2016.jpg' | relative_url }}" alt="" width="480" height="61" loading="lazy">
    Advances in Real-Time Rendering- SIGGRAPH 2016<br>
    advances.realtimerendering.com/s2016/
  </a>
</p>

---

## 1.建立织物着色器库
{: #h_718578091_0 }

在制作织物方面，工作人员遇到了一下的挑战：

1. 有非常多中不同的织物类型
2. 怎样去实现不同的反射率模型
3. 织物有较高的散射率
4. 可平铺的微编织结构
5. 体积自阴影
6. 添加一些缺陷不完美的细节来创建更真实的表现

### 微编制结构方面
{: #h_718578091_1 }

针对微编织结构，我们挑选了一些不同的图案，并将其在Maya中建模

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-01.png' | relative_url }}" alt="微编织结构的图案" width="986" height="448" loading="lazy">
  <figcaption>微编织结构的图案</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-02.png' | relative_url }}" alt="Maya中对编织图案建模" width="919" height="297" loading="lazy">
  <figcaption>Maya中对编织图案建模</figcaption>
</figure>

在对其进行建模的过程中，会先以图案的单个元素形状进行制作，然后复制模型，使用脚本对模型进行合并

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-03.png' | relative_url }}" alt="制作图案元素，Tilling后合并" width="871" height="326" loading="lazy">
  <figcaption>制作图案元素，Tilling后合并</figcaption>
</figure>

对于为什么不使用扫描的织物资产，一方面是为了节省贴图的内存，微编织结构的只需要64\*64的贴图大小，另一方面也可以保留微编织结构的细节而不用担心MipMap。此外我们一共有12种不同的微表面编织结构，4种不同的缺陷细节纹理，2种布料褶皱和老化方法，基于不同种类的细节纹理，调整Size做组合，我们可以实现大多数织物布料在现实的效果，而不必每种都使用扫描的办法。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-04.png' | relative_url }}" alt="只需要64*64的大小，即可Tilling" width="831" height="350" loading="lazy">
  <figcaption>只需要64*64的大小，即可Tilling</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-05.png' | relative_url }}" alt="细节占比高，不会因为MipMap导致细节丢失" width="879" height="371" loading="lazy">
  <figcaption>细节占比高，不会因为MipMap导致细节丢失</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-06.png' | relative_url }}" alt="不同纹理种类的组合以实现大多数织物的效果" width="739" height="306" loading="lazy">
  <figcaption>不同纹理种类的组合以实现大多数织物的效果</figcaption>
</figure>

以下是神秘海域4多种不同分辨率的可平铺细节叠加的材质预览效果，从基础的织物布料[BRDF](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=BRDF&zhida_source=entity)，添加微编织结构贴图，在添加织物老化和缺陷细节和褶皱后效果非常的真实。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-07.png' | relative_url }}" alt="织物材质的细节叠加" width="752" height="424" loading="lazy">
  <figcaption>织物材质的细节叠加</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-08.png' | relative_url }}" alt="织物材质的细节叠加" width="754" height="424" loading="lazy">
  <figcaption>织物材质的细节叠加</figcaption>
</figure>

除此之外，我们还用了UV2去添加布料的缝线和孔洞，可以达到更真实的效果。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-09.png' | relative_url }}" alt="添加布料的缝线和孔洞" width="769" height="383" loading="lazy">
  <figcaption>添加布料的缝线和孔洞</figcaption>
</figure>

### 织物的反射模型
{: #h_718578091_2 }

对于丝绸，丝绒和其它高反射的织物布料，我们同时尝试了GGX各向异性和[Kajiya-Kay](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=Kajiya-Kay&zhida_source=entity)两个Shading方法。GGX各向异性版本的效果要稍好，不过基于我们的光照模型，其实在大多数情况下比较难看出优势，所以我们选择了更性价比更好的Kajiya-Kay的版本。

对于棉布，羊毛材质，我们用了Ready at Dawn’s 工作室的布料反射模型并做了散射效果上的修改

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-10.png' | relative_url }}" alt="更廉价布料散射效果" width="1161" height="640" loading="lazy">
  <figcaption>更廉价布料散射效果</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-11.png' | relative_url }}" alt="在修改Shading后，布料会看起来比之前有更多的散射，更柔软" width="1160" height="655" loading="lazy">
  <figcaption>在修改Shading后，布料会看起来比之前有更多的散射，更柔软</figcaption>
</figure>

## 2.建立头发着色器库
{: #h_718578091_3 }

发丝是非常细且半透的物体，每根发丝都有不同的法线，并且发丝之间相互自阴影，为了使头发有体积感的表现，我们需要按照顺序来逐个解决这些问题。

PS4在性能上虽然有大幅度的提升，但是仍然不足达到实时渲染上百万根发丝的效果，因为有限的研发时间，我们也没有在[曲面细分着色器](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=%E6%9B%B2%E9%9D%A2%E7%BB%86%E5%88%86%E7%9D%80%E8%89%B2%E5%99%A8&zhida_source=entity)上研究太深，最终还是考虑使用发片（Hair Cards）的方式来制作头发

完全使用[AlphaBlend渲染](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=AlphaBlend%E6%B8%B2%E6%9F%93&zhida_source=entity)头发虽然会有一个非常好的效果，但会带来非常严重的OverDraw情况。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-12.png' | relative_url }}" alt="完全使用Alpha Blend会有大量的OverDraw" width="1058" height="455" loading="lazy">
  <figcaption>完全使用Alpha Blend会有大量的OverDraw</figcaption>
</figure>

因此对于绝大部分的头发，我们使用Dither Alpha并配合TAA。这会导致人物快速移动，有拖影的效果，为了避免这样的问题，我们调高头发的裁剪阈值，使得头发的发丝不那么薄和细。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-13.png' | relative_url }}" alt="使用Dither Alpha配合TAA会有拖影的情况" width="1105" height="466" loading="lazy">
  <figcaption>使用Dither Alpha配合TAA会有拖影的情况</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-14.png' | relative_url }}" alt="调高裁剪阈值，使得头发更粗来适配Dither和TAA" width="1160" height="650" loading="lazy">
  <figcaption>调高裁剪阈值，使得头发更粗来适配Dither和TAA</figcaption>
</figure>

但调高阈值后，会导致另外一个问题，头发看起来会有发片感。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-15.png' | relative_url }}" alt="头发有发片感" width="1161" height="651" loading="lazy">
  <figcaption>头发有发片感</figcaption>
</figure>

基于这样的观察，我们总结了一些导致发片感的原因，首先我们的发片使用了顶点法线，而不是单独的发丝法线，

其次，锐利的太阳光阴影使得头发看起来是一个不透明的物体，但是发丝其实是半透的。

## 头发处理
{: #h_718578091_4 }

基于以上的问题，3D艺术家在处理头发发片时，摆放的过程中，会让其更有一个体积块的视觉感

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-16.png' | relative_url }}" alt="体块处理" width="1072" height="418" loading="lazy">
  <figcaption>体块处理</figcaption>
</figure>

为了使得透射的效果更加的平滑，我们统一了发片的顶点法线（看起来像是对法线做了球面或者Mesh体块的映射效果），使得法线更统一，具有体块感。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-17.png' | relative_url }}" alt="统一法线" width="653" height="498" loading="lazy">
  <figcaption>统一法线</figcaption>
</figure>

### 头发阴影
{: #h_718578091_5 }

在头发阴影层面，如果减少阴影，会使得头发看起来太平面，不够立体。

我们尝试使用一组球形覆盖头模的灯光，来预计算头发的阴影，Bake到贴图中，该阴影是与方向光无关的的阴影（之前有尝试Bake多组不同方向光的信息，后来放弃未采用，只用LocalLight来烘培一个类似AO效果的阴影）

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-18.png' | relative_url }}" alt="球型覆盖灯光，烘培阴影" width="1440" height="811" loading="lazy">
  <figcaption>球型覆盖灯光，烘培阴影</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-19.png' | relative_url }}" alt="Bake Shadow" width="534" height="614" loading="lazy">
  <figcaption>Bake Shadow</figcaption>
</figure>

Bake Shadow使得头发看起来更有深度感，有体积感。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-20.png' | relative_url }}" alt="更好的头发质感" width="737" height="594" loading="lazy">
  <figcaption>更好的头发质感</figcaption>
</figure>

我们使用了两张贴图，一张1k贴图给发片共享细节，一张512的贴图用来存储Bake阴影，给到每个不同的发片不同的细节，Bake阴影使用UV2来存储信息。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-21.png' | relative_url }}" alt="两张细节纹理" width="1004" height="448" loading="lazy">
  <figcaption>两张细节纹理</figcaption>
</figure>

除了完全Bake的Shadow之外，还需要考虑其他物体投影到头发上的情况，如果只是做简单的乘法，头发的阴影看起来还是会比较平。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-22.png' | relative_url }}" alt="" width="1384" height="599" loading="lazy">
</figure>

我们需要减少在游戏中头发出现的硬阴影，简单的对shadow做blur其实特别耗费性能。在之前对发丝的处理中，我们调高了头发的裁剪阈值，使得发丝更粗，而对头发的Shadow我们可以使头发shadowpass的裁剪阈值重置，来使的Shadowpass的头发更细，这样Shadow就会更加柔和。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-23.png' | relative_url }}" alt="" width="1097" height="342" loading="lazy">
</figure>

这里对头发的shading做了一些调整，来使得头发的渲染更真实，

1. 对BakeShadow添加了[Light Wrap](https://zhida.zhihu.com/search?content_id=247814032&content_type=Article&match_order=1&q=Light+Wrap&zhida_source=entity)
2. 使用光照探针的强度和头发的颜色来控制BakeShadow

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-24.png' | relative_url }}" alt="修改Shadow的Shading计算" width="1101" height="527" loading="lazy">
  <figcaption>修改Shadow的Shading计算</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-25.png' | relative_url }}" alt="添加Bake Shadow前后" width="1095" height="437" loading="lazy">
  <figcaption>添加Bake Shadow前后</figcaption>
</figure>

### 头发的散射
{: #h_718578091_6 }

对于头发散射的两个关键元素，主要是发丝之间的散射和背光的散射效果。

对发丝间的散射我们用了和布料散射类似的方案，并且也有一个较好的效果

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-26.png' | relative_url }}" alt="" width="1073" height="454" loading="lazy">
</figure>

对于背光散射的情况，我可以将头发考虑成一个球体，我们可以发现背光散射的现象主要和灯光，相机角度，表面法线相关，散射的强度根据头发颜色、头发形状、头发长度和光照强度而变化。以下是神秘海域4给到的散射Shading计算，并给出的他们游戏中参数的参考值。 ScatterPower是一个幂参数，用于调整散射的菲尼尔形状，对于短发，在神秘海域4中是11，长发则为9。

lightScale 是我们根据头发的散射值选择的值。对于大多数金发，我们选择更高的值。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-27.png' | relative_url }}" alt="" width="1102" height="623" loading="lazy">
</figure>

### 头发着色模型
{: #h_718578091_7 }

在着色模型的选择上是标准的Kajiya-Kay，没啥好说的。

在高光的变化上，所有的材质球都会用一张可以平铺的specualr vairation mask，因为高光扰动会给玩家发丝的感觉，且发片 UV 布局统一。最后虽然该Mask并不能匹配所有的头发走向，但是这块产生的问题并不明显，对于 NPC 和多人游戏角色来说已经足够好了。

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-28.png' | relative_url }}" alt="KajiyaShading和Specualr Vairation Mask" width="1068" height="424" loading="lazy">
  <figcaption>KajiyaShading和Specualr Vairation Mask</figcaption>
</figure>

<figure>
  <img src="{{ '/assets/images/uncharted-4-cloth-and-hair/figure-29.png' | relative_url }}" alt="错误并不明显" width="849" height="438" loading="lazy">
  <figcaption>错误并不明显</figcaption>
</figure>

---
