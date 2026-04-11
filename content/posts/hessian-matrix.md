---
categories:
- Econometrics!!!
date: '2013-11-08T03:45:19+08:00'
draft: false
slug: hessian-matrix
tags: []
title: Hessian matrix
---

from wiki

In mathematics, the **Hessian matrix** or **Hessian** is a square matrix of second-order partial derivatives of a function. It describes the local curvature of a function of many variables.

Given the real-valued function

:   ![f(x_1, x_2, \dots, x_n),\,\!](http://upload.wikimedia.org/math/f/1/8/f180f6ef218ef931b5c2d30adade7623.png)

if all second partial derivatives of *f* exist and are continuous over the domain of the function, then the Hessian matrix of *f* is

:   ![H(f)_{ij}(\mathbf x) = D_i D_j f(\mathbf x)\,\!](http://upload.wikimedia.org/math/1/5/e/15ebe445e3b1d259ed5c70057cd5857c.png)

where ***x*** = (*x*1, *x*2, ..., *x*n) and *D*i is the differentiation operator with respect to the *i*th argument. Thus

:   ![H(f) = \begin{bmatrix}
    \dfrac{\partial^2 f}{\partial x_1^2} & \dfrac{\partial^2 f}{\partial x_1\,\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_1\,\partial x_n} \\[2.2ex]
    \dfrac{\partial^2 f}{\partial x_2\,\partial x_1} & \dfrac{\partial^2 f}{\partial x_2^2} & \cdots & \dfrac{\partial^2 f}{\partial x_2\,\partial x_n} \\[2.2ex]
    \vdots & \vdots & \ddots & \vdots \\[2.2ex]
    \dfrac{\partial^2 f}{\partial x_n\,\partial x_1} & \dfrac{\partial^2 f}{\partial x_n\,\partial x_2} & \cdots & \dfrac{\partial^2 f}{\partial x_n^2}
    \end{bmatrix}.](http://upload.wikimedia.org/math/f/7/2/f7296865484b39fcbac598a99b7f3dbb.png)

Because *f* is often clear from context, ![H(f)(\mathbf x)](http://upload.wikimedia.org/math/7/7/c/77c73786d1792c2863079cf10c6ab80a.png) is frequently abbreviated to ![H(\mathbf x)](http://upload.wikimedia.org/math/4/d/b/4dbbede3116928be8d6a27e087bfd451.png).

The Hessian matrix is related to the Jacobian matrix by ![H(f)(\mathbf x)](http://upload.wikimedia.org/math/7/7/c/77c73786d1792c2863079cf10c6ab80a.png) = ![J(\nabla \! f)(\mathbf x)](http://upload.wikimedia.org/math/0/d/c/0dcf72d3ed6f39a7064f51f3aa7853ac.png).

The determinant of the above matrix is also sometimes referred to as the Hessian.[\](http://en.wikipedia.org/wiki/Hessian_matrix#cite_note-1)

Hessian matrices are used in large-scale optimization problems within Newton-type methods because they are the coefficient of the quadratic term of a local Taylor expansion of a function. That is,

:   ![y=f(\mathbf{x}+\Delta\mathbf{x})\approx f(\mathbf{x}) + J(\mathbf{x})\Delta \mathbf{x} +\frac{1}{2} \Delta\mathbf{x}^\mathrm{T} H(\mathbf{x}) \Delta\mathbf{x}](http://upload.wikimedia.org/math/6/7/4/674dd1fa58cf748f3c71debf14a7cf1d.png)

where *J* is the Jacobian matrix, which is a vector (the gradient) for scalar-valued functions. The full Hessian matrix can be difficult to compute in practice; in such situations,quasi-Newton algorithms have been developed that use approximations to the Hessian. The best-known quasi-Newton algorithm is the BFGS algorithm.
