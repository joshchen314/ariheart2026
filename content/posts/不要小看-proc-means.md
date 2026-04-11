---
categories:
- SAS
date: '2013-11-01T06:45:02+08:00'
draft: false
slug: 不要小看-proc-means
tags: []
title: 不要小看 " proc means "
---

<http://sugiclub.blogspot.tw/2007/10/steps-to-success-with-proc-means.html>

1. 5個統計量可以不用經過特別的語法，就可以獲得：mean, std, n, max, min。

2. 控制變數及分類： var & class。

3. 加上條件： where\
> PROC MEANS DATA=SUGI.ELEC\_ANNUAL(WHERE=(REGION IN('WESTERN','SOUTHERN') and SUBSTR(RATE\_SCHEDULE,1,2) = 'E1')) MAXDEC = 0 MEAN SUM NONOBS;\
> VAR TOTKWH;\
> CLASS REGION RATE\_SCHEDULE;\
> title3 'Step 7: Take What You Need and Leave the Rest';\
> run;

\
4. 產出一個 DATA SET：\
> OUTPUT OUT=SUGI1

\
OR\
> OUTPUT OUT=SUGI2 sum(TOTREV TOTKWH) = sum\_rev sum\_kwh mean(TOTREV) = mean\_rev median(TOTHRS) = median\_hrs;

\
5. \_TYPE\_ 及 \_FREQ\_ (Step 11: Understanding \_TYPE\_ and \_FREQ\_)
