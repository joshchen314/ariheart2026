---
categories:
- SAS
date: '2013-10-29T02:07:07+08:00'
draft: false
slug: libname-與-data
tags: []
title: libname 與 data
---

基本上會是長得像下面的樣子：

1. **FILENAME** ALL104 'C:\SASEG\資料檔\dta08.TXT';
   白話講：藉**FILENAME** 指令將 'C:\SASEG\資料檔\dta08.TXT'檔案 命名為 ALL104
2. **LIBNAME**D104 'C:\Saseg\LIB\';
   白話講：藉**LIBNAME**指令將 'C:\Saseg\LIB\'路徑 命名為 D104

link: <http://www.pt.ntu.edu.tw/hmchai/SAS/SASdata/SAScreate.htm>
**data  lib名稱.sas7bdat檔名;**
以 data 指令建立符合只針對 SAS 格式的資料檔 ( \*.sas7bdat 檔)，並存在 libname 指定之資料夾路徑內。並且執行後可於 libnmae 指定之資料夾路徑內，找到這一筆 .sas7bdat 檔。
ex:   data ok.tens;
**proc print data=lib名稱.sas7bdat檔名;**呈現 .sas7bdat 資料檔內的資料，可以在 output 視窗中找到執行結果。也可將執行結果儲存成 \*.lst 的 ASCII 檔，之後就可以用其他軟體"烹調"了。注意：本指令的有**" = "**。
ex:
proc print data=ok.tens;
var id -- pain3;
title 'tens.sas7bdat data file';
 
**l****ibname lib名稱  '資料夾路徑';**使用本方法讀取資料前，**'資料夾路徑'**之中必須有sas7bdat格式資料檔。以 libname 指令為 library 命名，作為後續 SAS 程式資料夾路徑的縮寫。如大學裡有一棟放滿資料的library大樓(資料夾路徑)，命名為"總圖"("ok")，如下面的例子。
ex:  libname ok 'c:\SASex\';
也就是說，一旦產生資料後，可以將需要儲存的資料歸到 "ok" (在 libname 指定的資料夾路徑內)，得到一個索書碼 (SAS 資料檔 ，" \*.sas7bdat")。如另外使用 proc print 指令就不同，則輸出該資料至 output 視窗。
