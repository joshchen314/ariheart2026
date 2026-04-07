---
categories:
- SAS
date: '2013-10-30T06:55:20+08:00'
draft: false
slug: transpose
tags: []
title: transpose
---

proc transpose data=a out=d ;
by name; /\*藉由"name"轉置\*/
var item1-item4; /\*轉置的變項\*/
run;
