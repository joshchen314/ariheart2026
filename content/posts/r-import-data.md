---
categories:
- R
- R-Beauty
date: '2014-12-01T06:53:17+08:00'
draft: false
slug: r：import-data
tags: []
title: R：import data
---

為了製作Panel Data，可以在寫入資料時設定index鍵值，並且有兩種方法寫入變數。
1. 設定index鍵值：state，year
library(plm)
temp1=read.csv("D://6. R//...csv")
myData1= plm.data(temp1, index = c("state", "year"))
head(myData1)
2. 寫入變數
（1）直接設定
y=myData1[,3]
x1=myData1[,4]
x2=myData1[,5]
x3=myData1[,6]
x4=myData1[,7]
x5=myData1[,8]
x6=myData1[,9]
（2）LIST設定
Lhs= names(myData1)[3]
Rhs= paste(names(myData1)[4:9],collapse="+")
myEq=paste(Lhs, Rhs, sep="~")
myFormula=as.formula(myEq)
