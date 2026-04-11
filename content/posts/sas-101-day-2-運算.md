---
categories:
- SAS
- SAS 101
date: '2014-04-25T02:57:50+08:00'
draft: false
slug: sas-101-day-2-運算
tags: []
title: SAS 101 Day 2 Data階段：洗菜
---

這裡有兩個部分，數學運算與條件敘述。

一、行變量做數學運算\
以生成新變量（每一行，column）的方式做數學運算，也就是函數運算。

DATA agr1;\
set agr;\
avgItem= **MEAN**(Opening, Workers, Revenue, Etc);\
INTavgItem= **int**(avgItem);\
sumItem1= **sum**(of Opening, Workers, Revenue, Etc);  /\* 有缺失值仍正確 */\
sumItem2= Opening**+**Workers**+**Revenue**+**Etc;   /*  有缺失值會錯誤 \*/\
M1= **MAX**(Opening, Workers, Revenue, Etc);\
M2= **MIN**(Opening, Workers, Revenue, Etc);\
N1= **N**(Opening, Workers, Revenue, Etc);\
N2= **NMISS**(Opening, Workers, Revenue, Etc);\
lnOpening= **LOG**(Opening);\
lnWorkers= **LOG**(Workers);\
lnRevenue= **LOG**(Revenue);\
lnEtc= **LOG**(Etc);\
run;

若是要讓 資料（每一列，row）作函數運算，就要使用 proc 階段或proc 階段混搭 data 階段。

二、條件
1. **if  A  then  X  ;**
2. **if   A  and/or  B   then  X;**
3. **if A then do;**
X=asf;
Y=adaf;
**end;**
 **else if  B  then do;**
X=asd;
Y=asdd;
**end;**
