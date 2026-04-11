---
categories:
- SAS
date: '2013-11-11T03:59:58+08:00'
draft: false
slug: the-creating-of-dummy-variables
tags: []
title: the Creating of Dummy Variables
---

在 DATA 階段，可以製造出虛擬變數，數量是該類別的子數量減 1 ，如：教育程度有 3 類，小學、中學及大學，那虛擬變數設 2 個。

**DATA** Dmy;    SET TEST;\
ARRAY A {\*} edu1-edu2;  /\*虛擬變數多個\*/\
DO i = **1** TO **2**;\
A(i) = (edu=i);        /\*edu 為原始資料；edu= 1 為小學， 2 為中學， 3 為大學\*/\
END;
