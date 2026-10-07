---
layout: post
title: "3D数学基础：射线求交"
date: 2026-01-11 16:52:31 +0800
author: "DZPMX"
published: true
header-img: "assets/images/blog-cover.jpg"
no-catalog: false
tags:
  - 数学推导
typora-root-url: ../
typora-copy-images-to: ../assets/images/ray-intersectio
---

## 一、射线参数方程

已知射线的起点为 $O$，方向为 $D$，则射线上任意一点 $P$ 的位置可用参数方程表示为： $P=O+tD$。其中，$t$ 为参数，表示从起点 $O$ 出发，沿方向 $D$ 移动的距离。随着 $t$ 的变化，点 $P$ 在射线上移动。

## 二、射线与平面求交

已知平面上一点 $P_{0}$ 与非零法向量 $N$，平面上的任意点 $P$ 都满足：从 $P_{0}$ 指向 $P$ 的向量与 $N$ 垂直。因此，平面方程为：

$$
(P-P_{0})\cdot N=0
$$

射线的参数方程为 $P=O+tD$，其中 $D\neq0$，$t\geq0$，并将起点计入射线。要求射线与平面的交点，就需要找到同时满足这两个方程的点。

将 $P=O+tD$ 代入平面方程：

$$
(O+tD-P_{0})\cdot N=0
$$

展开点乘：

$$
(O-P_{0})\cdot N+t(D\cdot N)=0
$$

将与 $t$ 无关的项移到右侧：

$$
t(D\cdot N)=(P_{0}-O)\cdot N
$$

求解 $t$ 前，先判断其系数 $D\cdot N$ 是否为 0。

当 $D\cdot N=0$ 时，射线方向平行于平面，上式左侧恒为 0。此时根据右侧的值，可分为两种情况：

- 若 $(P_{0}-O)\cdot N\neq0$，则等式无法成立，不存在满足条件的 $t$，射线与平面不相交。
- 若 $(P_{0}-O)\cdot N=0$，则任意 $t\geq0$ 都满足等式。射线起点在平面上，整条射线也都在平面内，属于共面情况，没有唯一交点。

当 $D\cdot N\neq0$ 时，射线方向不平行于平面，可以在等式两侧同时除以 $D\cdot N$，得到：

$$
t=\frac{(P_{0}-O)\cdot N}{D\cdot N}
$$

这个解对应射线所在直线与平面的唯一交点。由于射线只包含 $t\geq0$ 的部分，还需要检查求得的 $t$：

- 若 $t<0$，交点位于射线反方向的延长线上，射线本身不与平面相交。
- 若 $t=0$，交点就是射线起点 $O$。
- 若 $t>0$，交点位于射线起点前方。

因此，在 $D\cdot N\neq0$ 且 $t\geq0$ 时，射线与平面有唯一交点。最后将求得的 $t$ 代回射线参数方程，即可得到交点的位置：

$$
P=O+tD
$$

## 三、射线与三角形求交

要判断射线是否与三角形相交，可以先判断射线是否与三角形所在的平面相交。如果相交，再判断交点是否在三角形内，进而得出结论。

首先需要确定三角形所在的平面。假设三角形由三个顶点 $P_{0},P_{1},P_{2}$ 确定，则其所在平面的法向量为 $N=Normalize((P_{1}-P_{0})\times(P_{2}-P_{0}))$

接着，使用上一节的方法求射线与该平面的交点。若判定为不相交，则射线也不与三角形相交；若判定为共面，则需要单独处理平面内的射线与三角形求交。以下继续讨论射线与平面存在唯一交点的情况。

此时已知射线与平面的交点 $P$，如下图所示：

<figure>
  <img src="/assets/images/ray-intersection/figure-01.png" alt="" loading="lazy" width="360" style="width: 360px; max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto;">
</figure>

沿三角形的三条边，按顺时针或逆时针方向构造三个向量，则点 P 必然在三个向量方向的同一侧。以顺时针为例，可以分别计算 $(P_{2}-P_{1})\times( P-P_{1})$ 、$(P_{1}-P_{0})\times( P-P_{0})$ 、$(P_{0}-P_{2})\times( P-P_{2})$ 这三个叉乘结果，并判断其符号是否相同；相同则表示交点在三角形内。

## 四、射线与球体求交

已知球体的球心为 $C$，半径为 $r$，则球面上任意一点 $P$ 到球心的距离必然等于半径 $r$，用公式表示为：$\left| P-C \right|=r$。

已知向量的点乘公式为 $a\cdot b=\left| a \right| \times \left| b \right|\times cos\theta$，当向量 $a$ 和向量 $b$ 相等时， $cos\theta$ 为 1，则有 $a\cdot a=\left| a \right| \times \left| a \right|$，由此得到球面方程 $(P-C)\cdot(P-C)=r^{2}$

将射线参数方程中的 P 代入球面方程，可得 $(O+tD-C)\cdot(O+tD-C)=r^{2}$

记向量 $O-C$ 为 $\vec{CO}$，则有 $( \vec{CO} +tD)\cdot( \vec{CO} +tD)=r^{2}$

展开后有 $tD\cdot tD+2\vec{CO}\cdot tD+\vec{CO}\cdot\vec{CO}=r^{2}$

提取 t 并移项，可得 $t^{2}(D\cdot D)+2t(\vec{CO}\cdot D)+(\vec{CO}\cdot\vec{CO})-r^{2}=0$

对照一元二次方程 $ax^{2}+bx+c=0$，用 $x$ 表示 $t$，则 $a=(D\cdot D)$，$b=2(\vec{CO}\cdot D)$，c = $(\vec{CO}\cdot \vec{CO})-r^{2}$

根据韦达定理，可通过 $\frac{-b\pm \sqrt{b^{2}-4ac}}{2a}$ 求得 t 的值。

## 五、射线与 AABB 求交

对于 AABB，一般用两个角点来表示：

$$
\begin{align} \text{最小角（左下后）}\quad \mathbf{B}_{\min} &= (x_{\min},\, y_{\min},\, z_{\min}) \\ \text{最大角（右上前）}\quad \mathbf{B}_{\max} &= (x_{\max},\, y_{\max},\, z_{\max}) \end{align}
$$

当点 $（x,y,z）$ 在盒子里时，必须满足 

$$
x_{\min} \le x \le x_{\max},\quad y_{\min} \le y \le y_{\max},\quad z_{\min} \le z \le z_{\max}
$$

可以把盒子想象成由三组“夹板”夹出来的空间：

x 方向的两个平面：$x = x_{\min} 和 x = x_{\max}$

y 方向的两个平面：$y = y_{\min} 和 y = y_{\max}$

z 方向的两个平面：$z = z_{\min} 和 z = z_{\max}$

射线要进入盒子，必须同时满足：在某段时间 $t$ 内，$x$ 落在 $[x_{\min},\, x_{\max}]$，$y$ 落在 $[y_{\min},\, y_{\max}]$，$z$ 落在 $[z_{\min},\, z_{\max}]$

以点 $P$ 为例，可以先推导 $P$ 在 $x$ 轴上所在的区间。

此时要求 $x_{\min} \leq P_{x}\leq x_{\max}$，代入射线方程，则有：

$$
x_{\min} \le O_x + tD_x \le x_{\max}
$$

$$
x_{\min} - O_x \le tD_x \le x_{\max} - O_x
$$

两边同时除以 $D_x$

$D_x>0$：

$$
\frac{x_{\min}-O_x}{D_x} \le t \le \frac{x_{\max}-O_x}{D_x}
$$

$D_x=0$：则 $x=O_x$。如果 $O_x$ 本身在 $[x_{\min},\, x_{\max}]$，则 x 轴没有额外限制，永远在 AABB 内；如果 $O_x$ 不在，则永不相交。

$D_x<0$：

$$
\frac{x_{\max}-O_x}{D_x} \le t \le \frac{x_{\min}-O_x}{D_x}
$$

其他两个轴向同理。计算后会得到：

$[t_{x\min},\, t_{x\max}]，[t_{y\min},\, t_{y\max}]，[t_{z\min},\, t_{z\max}]$

三个区间重叠的时间段为  
 $t_{\text{enter}}=\max\!\left(t_{x\min},\,t_{y\min},\,t_{z\min}\right)$   
 $t_{\text{exit}}=\min\!\left(t_{x\max},\,t_{y\max},\,t_{z\max}\right)$

只要进入时间不晚于离开时间，就说明有重叠，即 $t_{\text{enter}} \le t_{\text{exit}}$。同时，对于射线，只考虑 $t\geq0$。

代入射线参数方程，即可得到 AABB 的入射点与出射点。
