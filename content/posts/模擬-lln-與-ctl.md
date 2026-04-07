---
categories:
- R-Beauty
date: '2013-11-05T01:17:26+08:00'
draft: false
slug: 模擬-lln-與-ctl
tags: []
title: '[模擬] LLN 與 CTL'
---

由4個方式產生亂數表，也就是資料庫，接著在每一次模擬時，找平均數作 LLN 的模擬，在模擬 CTL 時再作標準化。
-----------------------------------------------------------------------------------
#(1) LLN (50, 100, 200, 500)
#a. normal
# t is sample size
# n is repetition time
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rnorm(t))
}
x
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(-1,1),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(-1,1),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(-1,1),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(-1,1),freq=FALSE,main='T=500',xlab='Sample Mean')
#b. t(1)
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rt(t, df=1))
}
x
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(-10,10),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(-10,10),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(-10,10),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(-10,10),freq=FALSE,main='T=500',xlab='Sample Mean')
#c. t(3)
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rt(t, df=3))
}
x
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(-2,2),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(-2,2),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(-2,2),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(-2,2),freq=FALSE,main='T=500',xlab='Sample Mean')
#d. chi(5)
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rchisq(t,df=5))
}
x
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(0,7),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(0,7),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(0,7),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(0,7),freq=FALSE,main='T=500',xlab='Sample Mean')
#e. lognorm
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rlnorm(t, meanlog = 0, sdlog = 1))
}
x
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(0,4),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(0,4),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(0,4),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(0,4),freq=FALSE,main='T=500',xlab='Sample Mean')
------------------------------------------------------------------------------------------------
#(2) CLT (50, 100, 200, 500)
##a. normal
rm(list=ls(all=TRUE));
fn\_CLT<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rnorm(t))
}
(x-0)/(1/(t^(1/2)))
}
par(mfrow=c(2,2))
hist(fn\_CLT(50,5000),xlim=range(-5,5),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_CLT(100,5000),xlim=range(-5,5),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_CLT(200,5000),xlim=range(-5,5),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_CLT(500,5000),xlim=range(-5,5),freq=FALSE,main='T=500',xlab='Sample Mean')
##b. t(1)
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
sample <- rt(t,2)
x[i] <-  mean(sample)
x[i] <- (x[i]-0)/(sd(sample)/(t^(1/2)))
}
x
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(-10,10),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(-10,10),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(-10,10),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(-10,10),freq=FALSE,main='T=500',xlab='Sample Mean')
##因為t(2)無母體變異數，以樣本變異數取代母體變異數##
##c. t(3)
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
sample <- rt(t,3)
x[i] <-  mean(sample)
x[i] <- (x[i]-0)/(3^(1/2)/(t^(1/2)))
}
x
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(-6,6),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(-6,6),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(-6,6),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(-6,6),freq=FALSE,main='T=500',xlab='Sample Mean')
##d. chi(5)
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rchisq(t,df=5))
}
(x-5)/(((2\*5)^(1/2))/(t^(1/2)))
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(-5,5),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(-5,5),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(-5,5),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(-5,5),freq=FALSE,main='T=500',xlab='Sample Mean')
##e. lognorm
rm(list=ls(all=TRUE));
fn\_LLN<-function(t,n){
x<-numeric(n)
for(i in 1:n){
x[i] <- mean(rlnorm(t, meanlog = 0, sdlog = 1))
}
(x-0)/(1/(t^(1/2)))
}
par(mfrow=c(2,2))
hist(fn\_LLN(50,5000),xlim=range(0,60),freq=FALSE,main='T=50',xlab='Sample Mean')
hist(fn\_LLN(100,5000),xlim=range(0,60),freq=FALSE, main='T=100',xlab='Sample Mean')
hist(fn\_LLN(200,5000),xlim=range(0,60),freq=FALSE,main='T=200',xlab='Sample Mean')
hist(fn\_LLN(500,5000),xlim=range(0,60),freq=FALSE,main='T=500',xlab='Sample Mean')
