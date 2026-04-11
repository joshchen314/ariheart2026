---
categories:
- SAS
- SAS-Beauty
date: '2014-03-07T03:52:01+08:00'
draft: false
slug: sas-dummy-variable-再應用
tags: []
title: 'SAS: Dummy Variable 再應用'
---

在 SAS 資料處理的時候，會有變數及類別要加總，或生成新的欄位。如下所示：\

\
\
|\
  |\
 變數 |\
 COL1 |\
 COL2 |\

\
|\
 類別 |\
  |\
  |\
  |\

\
|\
  |\
  |\
  |\
  |\

\
\

\
如果資料本身是 1 個變數，裡頭有 9 個子項目。這裡有一個例子，有個變數叫"主要服務項目代號"，裏面有 16 種服務，像是 "01 稻作"、"02 雜糧" 等。如果我要計算各種服務的次數，且選擇加總的方式，通常我會假設"01 稻作"為"COL1"、"02 雜糧"為"COL2"等類推。

一般作法是一個接著一假設的苦力法。

還有就是利用生成"DUMMY VARIABLE"的方法。如下：

ARRAY dummys{16} COL1 - COL16;\
DO i=1 TO 16;\
dummys(i) = 0;\
END;\
dummys(主要服務項目代號) = 1;

接著只要在 PROC SUMMARY 階段，加總 COL1 到 COL16，就可以得到各子項目的總數了。太漂亮了！
