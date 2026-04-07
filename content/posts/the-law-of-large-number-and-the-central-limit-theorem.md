---
categories:
- SAS-Beauty
date: '2013-10-31T05:34:45+08:00'
draft: false
slug: the-law-of-large-number-and-the-central-limit-theorem
tags: []
title: the Law of Large Number and the Central Limit Theorem
---

一開始，先用標準常態跑出亂數表，按需要的樣本數，產生同等數量的亂數，然後塞進 "array" 裡面，類似一個矩陣。
----------------------------------------------------------------------
DATA one;
array n{50} n1-n50; \* a row represents a sample of size 50;
do sample = 1 to 1000; \*generate 1000 samples;
do i = 1 to 50;
n[i] = rannor(i);
end;
meana = mean(of n1-n50); \*1000 sample means computed;
output;
end;
run;
ods graphics on;
proc chart;
vbar meana;
proc univariate data = one;
histogram meana/normal;
run;
-------------------
