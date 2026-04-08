---
categories:
- R
- R-Beauty
date: '2013-11-01T07:46:49+08:00'
draft: false
slug: the-law-of-large-number
tags: []
title: the Law of Large Number
---

這裡是用R統計軟體驗證the Law of Large Number。
--------------------------------
# t is sample size
# n is repetition time
rm(list=ls(all=TRUE));
fun\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rnorm(t))
}
x
}
par(mfrow=c(2,2))
hist(fun\_LLN(50,5000),xlim=range(-1,1),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fun\_LLN(100,5000),xlim=range(-1,1),freq=FALSE, main='T=100',
xlab='Sample Mean')
hist(fun\_LLN(200,5000),xlim=range(-1,1),freq=FALSE,main='T=200',
xlab='Sample Mean')
hist(fun\_LLN(500,5000),xlim=range(-1,1),freq=FALSE,main='T=500',
xlab='Sample Mean')
------------------------------------ beautiful ---------------------------------------
[![LLN_R](../../images/2013/lln_r.png)](../../images/2013/lln_r.png)
