---
categories:
- Econometrics!!!
date: '2013-11-05T10:27:12+08:00'
draft: false
slug: covariance-matrix
tags: []
title: Covariance matrix
---

from wiki
假設![X](http://upload.wikimedia.org/math/0/2/1/02129bb861061d1a052c592e2dc6b383.png)是以![n](http://upload.wikimedia.org/math/7/b/8/7b8b965ad4bca0e41ab51de7b31363a1.png)個純量隨機變數組成的 Column vector，

:   ![X = \begin{bmatrix}X_1 \\  \vdots \\ X_n \end{bmatrix}](http://upload.wikimedia.org/math/9/4/a/94a2f6bfacd447458d679ce5a3931cea.png)

並且 ![\mu_i](http://upload.wikimedia.org/math/a/0/e/a0e6978ffc1dc7ff965069c2f7e183f2.png) 是其第*i*個元素的期望值，即  ![\mu_i = \mathrm{E}(X_i)](http://upload.wikimedia.org/math/d/d/6/dd65c3a62f4f550d0572efada591bad6.png)。 共變異數矩陣被定義的第 i，j 項是如下：

:   ![\Sigma_{ij}
    = \mathrm{cov}(X_i, X_j) = \mathrm{E}\begin{bmatrix}
    (X_i - \mu_i)(X_j - \mu_j)
    \end{bmatrix}](http://upload.wikimedia.org/math/5/a/5/5a5863e88a72a8e4b8215e7ad79c842b.png)

即：

:   ![\Sigma=\mathrm{E}
    \left[
     \left(
     \textbf{X} - \mathrm{E}[\textbf{X}]
     \right)
     \left(
     \textbf{X} - \mathrm{E}[\textbf{X}]
     \right)^\top
    \right]](http://upload.wikimedia.org/math/1/8/1/1811f942680a72974597be42c28d31d2.png)

:   :   ![=
        \begin{bmatrix}
         \mathrm{E}[(X_1 - \mu_1)(X_1 - \mu_1)] & \mathrm{E}[(X_1 - \mu_1)(X_2 - \mu_2)] & \cdots & \mathrm{E}[(X_1 - \mu_1)(X_n - \mu_n)] \\ \\
         \mathrm{E}[(X_2 - \mu_2)(X_1 - \mu_1)] & \mathrm{E}[(X_2 - \mu_2)(X_2 - \mu_2)] & \cdots & \mathrm{E}[(X_2 - \mu_2)(X_n - \mu_n)] \\ \\
         \vdots & \vdots & \ddots & \vdots \\ \\
         \mathrm{E}[(X_n - \mu_n)(X_1 - \mu_1)] & \mathrm{E}[(X_n - \mu_n)(X_2 - \mu_2)] & \cdots & \mathrm{E}[(X_n - \mu_n)(X_n - \mu_n)]
        \end{bmatrix}](http://upload.wikimedia.org/math/a/1/2/a12a573ecd1d853abd8c01fab9fccfbe.png)

矩陣中的第 ![(i,j)](http://upload.wikimedia.org/math/5/2/7/5270ae675fac24f97e172dcd9b18fa92.png) 個元素是  ![X_i](http://upload.wikimedia.org/math/4/f/c/4fc3e3c98d13ed389817f11dc66c10a6.png)  與  ![X_j](http://upload.wikimedia.org/math/1/b/e/1be03680765d1758574e1a99d121e1bf.png)  的共變異數。
 
###性質
![\Sigma=\mathrm{E} \left[ \left( \textbf{X} - \mathrm{E}[\textbf{X}] \right) \left( \textbf{X} - \mathrm{E}[\textbf{X}] \right)^\top \right]](http://upload.wikimedia.org/math/1/8/1/1811f942680a72974597be42c28d31d2.png)  與  ![ \mu = \mathrm{E}(\textbf{X})](http://upload.wikimedia.org/math/2/c/4/2c43445d2a0366e7e90bc8cdf0318468.png)   滿足下邊的基本性質：

1. ![ \Sigma = \mathrm{E}(\mathbf{X X^\top}) - \mathbf{\mu}\mathbf{\mu^\top} ](http://upload.wikimedia.org/math/6/7/6/67616c643a158c1e00a8e4d5ec3d0b1a.png)
2. ![ \operatorname{var}(\mathbf{a^\top}\mathbf{X}) = \mathbf{a^\top} \operatorname{var}(\mathbf{X}) \mathbf{a} ](http://upload.wikimedia.org/math/d/2/8/d28c8e969e6ee190cdf1df9e5872c9c4.png)
3. ![ \mathbf{\Sigma} \geq 0 ](http://upload.wikimedia.org/math/d/0/d/d0df9f0af75fbe243837ef52efb2662b.png)
4. ![ \operatorname{var}(\mathbf{A X} + \mathbf{a}) = \mathbf{A} \operatorname{var}(\mathbf{X}) \mathbf{A^\top} ](http://upload.wikimedia.org/math/e/4/3/e4324195590bceb42f39531bf802187b.png)
5. ![ \operatorname{cov}(\mathbf{X},\mathbf{Y}) = \operatorname{cov}(\mathbf{Y},\mathbf{X})^\top](http://upload.wikimedia.org/math/4/f/6/4f6b43e1a9be66f6c79a7b3ae3332326.png)
6. ![ \operatorname{cov}(\mathbf{X_1} + \mathbf{X_2},\mathbf{Y}) = \operatorname{cov}(\mathbf{X_1},\mathbf{Y}) + \operatorname{cov}(\mathbf{X_2}, \mathbf{Y})](http://upload.wikimedia.org/math/2/8/4/2847bf6a626a608178fbf3062964dfc5.png)
7. 若 ![p = q](http://upload.wikimedia.org/math/6/a/b/6ab113c9c0248fb17eda1c4e6e8077c5.png)，則有![\operatorname{cov}(\mathbf{X} + \mathbf{Y}) = \operatorname{var}(\mathbf{X}) + \operatorname{cov}(\mathbf{X},\mathbf{Y}) + \operatorname{cov}(\mathbf{Y}, \mathbf{X}) + \operatorname{var}(\mathbf{Y})](http://upload.wikimedia.org/math/1/a/7/1a7cb39262f833ab2a0583a1a3b166a6.png)
8. ![\operatorname{cov}(\mathbf{AX}, \mathbf{BX}) = \mathbf{A} \operatorname{cov}(\mathbf{X}, \mathbf{X}) \mathbf{B}^\top](http://upload.wikimedia.org/math/f/0/5/f0502a8fd4bd4018002e2b7bcb557f14.png)
9. 若![\mathbf{X}](http://upload.wikimedia.org/math/5/9/8/598f6444904755dda4a859a1e377468e.png) 與![\mathbf{Y}](http://upload.wikimedia.org/math/f/7/d/f7d28a30784c2b10b8fc16ab9575482b.png) 是獨立的，則有![\operatorname{cov}(\mathbf{X}, \mathbf{Y}) = 0](http://upload.wikimedia.org/math/6/8/9/689c148e2df58bc50f6f966189e35a11.png)
10. ![ \Sigma = \Sigma^\top ](http://upload.wikimedia.org/math/b/5/f/b5f94be299cd195bf63f8ccbd1a0ada7.png)

其中  ![\mathbf{X}, \mathbf{X_1}](http://upload.wikimedia.org/math/b/8/b/b8bea0cf8954e514cc649d86d79f9f63.png)  與  ![\mathbf{X_2}](http://upload.wikimedia.org/math/7/8/6/78669d999a34ce09717c8767152250c2.png)   是隨機  ![\mathbf{(p \times 1)}](http://upload.wikimedia.org/math/3/6/6/366be9c7025f45ee5c5bfe2190c167be.png)  向量,   ![\mathbf{Y}](http://upload.wikimedia.org/math/f/7/d/f7d28a30784c2b10b8fc16ab9575482b.png)   是隨機  ![\mathbf{(q \times 1)}](http://upload.wikimedia.org/math/2/5/7/2572dfbdc63874f9d603d4827b435182.png)  向量,   ![\mathbf{a}](http://upload.wikimedia.org/math/3/c/4/3c47f830945ee6b24984ab0ba188e10e.png) 是  ![\mathbf{(p \times 1)}](http://upload.wikimedia.org/math/3/6/6/366be9c7025f45ee5c5bfe2190c167be.png)   向量,   ![\mathbf{A}](http://upload.wikimedia.org/math/9/2/5/92555f9439ef4a54fcd65bd62f44f4ee.png)   與  ![\mathbf{B}](http://upload.wikimedia.org/math/4/1/9/41968d7938b8145f26e1d196abc77144.png)   是  ![\mathbf{(q \times p)}](http://upload.wikimedia.org/math/1/d/3/1d386387535e2d43a03d149476cef883.png)   矩陣。
 
###NOTE: 線性代數的視覺化、炫麗化效果是，矩陣。所以，我應該多多把矩陣畫開來，有足夠的視覺化，就能有足夠的感覺體會計量經濟學。
