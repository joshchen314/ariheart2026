---
categories:
- SAS
date: '2013-11-01T08:05:50+08:00'
draft: false
slug: array-made-easy-hope-so
tags: []
title: array made easy? hope so.
---

<http://sugiclub.blogspot.tw/2007/03/arrays-made-easy-introduction-to-arrays.html>

陣列語法：\
> **array array-name {n} <$> length array-elements (initial-values);**

\
設定是：\
1. array-name  名稱\
2. n  大小\
3. $  指定字串變數\
4. length  變數長度\
5. elements 輸入一連串變數名稱\
6. initial values  起始值\
7. 可以用 \_NUMERIC\_，一次代入所有數值變數。\
8. 每個陣列只能在某一個 Data step 中使用，其他的不能使用，相當受限制。

ex: array temperature\_array {24} temp1 – temp24;\
array allnums {\*} \_numeric\_;

目地：強大的簡化功能

1.一筆一筆更正：\
data;\
input etc.\
celsius\_temp1 = 5/9(temp1 – 32);\
celsius\_temp2 = 5/9(temp2 – 32);\
. . .\
celsius\_temp24 = 5/9(temp24 – 32);\
run;

2. beautiful and powerful array：\
data;\
input etc.\
array temperature\_array {24} temp1-temp24;\
array celsius\_array {24} celsius\_temp1-celsius\_temp24;\
do i = 1 to 24;\
celsius\_array{i} = 5/9(temperature\_array{i} – 32);\
end;\
run;
