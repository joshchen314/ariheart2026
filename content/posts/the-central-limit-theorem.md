---
categories:
- R
- R-Beauty
date: '2013-11-01T09:12:23+08:00'
draft: false
slug: the-central-limit-theorem
tags: []
title: the Central Limit Theorem
---

rm(list=ls(all=TRUE));\
fn\_CLT<-function(t,n){\
x<-numeric(n)\
for(i in 1:n){\
x[i] <- mean(rnorm(t))\
}\
(x-0)/(1/(t^(1/2)))\
}\
par(mfrow=c(2,2))\
hist(fn\_CLT(50,5000),xlim=range(-5,5),freq=FALSE,main='T=50',xlab='Sample Mean')\
hist(fn\_CLT(100,5000),xlim=range(-5,5),freq=FALSE, main='T=100',xlab='Sample Mean')\
hist(fn\_CLT(200,5000),xlim=range(-5,5),freq=FALSE,main='T=200',xlab='Sample Mean')\
hist(fn\_CLT(500,5000),xlim=range(-5,5),freq=FALSE,main='T=500',xlab='Sample Mean')

----------------------------------------gorgeous------------------------------------------

[![CLT_R](../../images/2013/clt_r.png)](../../images/2013/clt_r.png)

------------------------------------[?] a problem [?]-----------------------------------

50: In x[i] <- rnorm(t) :\
number of items to replace is not a multiple of replacement length

正確的想法應該是：先找出每一次模擬的統計量平均數，再將之標準化。
