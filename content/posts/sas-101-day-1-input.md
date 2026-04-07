---
categories:
- SAS
- SAS 101
date: '2014-04-25T02:55:52+08:00'
draft: false
slug: sas-101：-day-1-input
tags: []
title: SAS 101 Day 1 SAS是吃貨嗎 -- 買菜放進冰箱
---

受到高手啟發，因此瞭解自己寫程式要到什麼程度，才算"會"寫程式，如 SAS，或 R。因為自己不是科班出身，預期自己能夠寫出什麼簡潔、高效的語法根本天方夜譚，不切實際。想通之後，我的第一目標是只要能夠用程式滿足大部分工作的要求，不是對該程式語言達到精熟。也就是說，我追求的是堪用。所以， SAS 101 系列是紀錄自己常用到、可能用到的部分語法，方便自己在一陣子不用後，只要瀏覽本系列，就能夠快速上手。最後，高手在這：
1. [前輩](http://r97846001.blog.ntu.edu.tw/2010/07/11/sas-macro_introduction/)
2. [落園](http://http://www.loyhome.com/learn-sas-in-7-days-index/)3.[SUGI CLUB](http://sugiclub.blogspot.tw/search/label/%E7%A8%8B%E5%BA%8F%E8%AA%9E%E6%B3%95)

如果要用SAS來處理資料，第一步要做的當然是將資料讀入。同時，也藉著讀取資料做為例子，瞭解SAS程式寫作風格，就是 " ; " 與 " run; " 。開宗明義，每一行程式語法基本都是以 " ; "結尾（除了因為程式可讀性而斷行的原因沒有" ; "結尾）；SAS語法結構基本上由 DATA階段（[DAY 2](https://ariheart2011.wordpress.com/2014/04/25/sas-101-day-2-%E9%81%8B%E7%AE%97/)）與 PROC階段（[DAY 3](https://ariheart2011.wordpress.com/2014/04/25/sas-101-day-3-%E7%83%B9%E8%AA%BF/)）組成，每個階段結束部分都加上 " run; " ，比較能夠避免錯誤。
進入主題，主要會有兩種讀取檔案的方式，csv與文字檔案。為了以後方便使用，可以使用libname存起來。

1. **DATA 階段讀取csv檔:**
   生成一組資料，命名為” io.csv”存進 C 的資料夾，位置在” c:\MyRawData\io.csv”。建立的方法是，打開 "記事本"，把下欄資料存進去，檔名存成 " io.csv "，就有資料了。（最近感觸很深，讀了一本介紹 R 與統計觀念的書，結果居然沒有 source code，這就算了，連 raw data 都沒有，真是情何以堪哪。還好，我是跟學校借的，不然一本約3,000元左右，真的是出不起。）

|  |
| --- |
| agriculture,1/23/2010,5,9,5,99 fishery,1/25/2010,7,7,7,45 forestry,1/15/2010,3,4,4,21 animal husbandry,1/18/2010,14,12,31,2 |

|  |
| --- |
| **DATA** agr; INFILE 'c:\MyRawData\io.csv'   DLM =','   DSD MISSOVER; INPUT BandName:$30. GigDate:MMDDYY10. Opening Workers Revenue Etc; RUN; **PROC****PRINT**DATA = agr; TITLE 'Analysiss of Agriculture'; **RUN**; |

其實，在data階段就讀csv進SAS了，命名為”agr”。之後可以直接調用了。細節如下：
INFILE 讀進檔案
INPUT  讀進檔案裡的資料，並且可以設定格式

2. **文字檔案**

|  |
| --- |
| /\*定義資料名稱及來源\*/ **FILENAME** a4  'D:\abcd.txt'; **LIBNAME** D099 'D:\-----'; **data** D099.HUS; infile a4 lrecl=**521**; input @**1** D000000 $CHAR13. @**14** D010001 1.;          /\* 最後一筆再加上" ; " \*/ run; |

細節如下：
**Filename** 白話講：藉 **FILENAME** 指令將 'D:\abcd.txt'檔案 命名為 ALL104。不讀檔案，只有為檔案命名，這裡命名為”a4”。
**Libname** 白話講：藉 **LIBNAME**指令將 'D:-----'路徑 命名為 D104。不讀檔案，只有為檔案路徑設定成”擴展名”，這裡命名為”D099”。在使用之前，必須先有sas7bdat格式資料集，以本例來說，該檔案路徑已經有HUS的資料集，當我要使用的時候不用描述完整的檔案路徑，只要寫 ”D099.HUS”。
**infile**後面跟著所讀的檔名，本例是以 **LIBNAME**指令來讀取資料集。
**lrecl** 是每一筆資料的長度，這裡是 521個 BYTES。
**@1 D000000 $CHAR13.**   @**1**表示從哪一個位置開始，D000000 是為變數取名字，而$CHAR13.的意思是文字格式與長度，如果只是數字就不用"$CHAR"。
 
**3. proc階段讀取CSV檔與XLSX檔**
型態：**PROC IMPORT** DATAFILE="C:\SASeg\r4.csv" OUT=r4s replace DBMS= CSV;
白話講：藉**PROC IMPORT**指令讀取"C:\SASeg\r4.csv"檔案，命名為 r4s
proc import中，方法的宣告、DATAFILE、OUT、DBMS其實是同一行，同一個敘述，只需要一組 " ; "，但是，為了程式可讀性，分為3行。此方法可以讀取 CSV、XLSX，需要在 DBMS 中設定。"getnames=yes;" 可以保留原始檔案的表頭資料。以下為程式：
libname ok 'c:\SASex\';
proc import DATAFILE="C:\SASex\reach14.csv"
OUT=ok.reach
DBMS= CSV replace;
getnames=yes;   /\* 原來有這一招，保留項目名稱 \*/
run;
proc print data=ok.reach;
var id -- angle4;
run;
/\* out=lib名稱.sas7bdat檔名 將讀取的 EXCEL.csv 資料檔，製成 只針對 SAS 格式的資料檔(.sas7bdat)，並存在 libname 指定的資料夾路徑內。 \*/
 
 
NOTE:  關於 SAS 語法結構，簡單講只有兩個階段 DATA階段與 PROC階段。這兩個階段截然不同，彼此獨立，互不牽涉，絕對互不包含。DATA階段主要在資料處理、讀取列資料，生成行變量等的資訊處理。PROC階段就是重在運算，如敘述性統計分析，回歸分析等。
