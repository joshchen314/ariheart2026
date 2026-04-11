---
categories:
- SAS
date: '2013-10-31T01:26:57+08:00'
draft: false
slug: simulation
tags: []
title: Simulation
---

 EX：N(20,0,1)\
DATA normal20;\
DO n=1 to 20;\
x=RANNOR(n);\
OUTPUT;\
END:

 EX：100 X N(20,0,1)\
DATA one;\
ARRAY q {\*} q1-q100;\
ARRAY k {\*} k1-k100;\
DO n=1 TO 20;\
i=1;\
DO i=1 to 100;\
k(i)=RANNOR(i);\
END;\
OUTPUT;\
END:\
RUN;
