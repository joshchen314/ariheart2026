---
categories:
- SAS
- SAS 101
date: '2014-04-25T03:08:46+08:00'
draft: false
slug: sas-101-day-3-烹調
tags: []
title: SAS 101 Day 3 Proc階段：烹調
---

這裡有兩個部分，先說 proc 階段都可以做的動作，再來是關於 proc 階段幾種常用的模式。

動作1：where

可以想成條件句來運用，也可以想成是求取子集合。

動作2：var

針對哪些變量作烹調。

動作3：class

分階層進行模式的烹調。如summary 模式下，會分階層加總。

動作4：sort

排序，搭配”by”決定優先順序的依據。如：proc sort data= ; by opening;。

動作5：print

就是輸出了。

動作6：format

一般用法，設定變量的格式，讓其統一。

|  |
| --- |
| **PROC PRINT DATA = sales;** VAR Name DateReturned CandyType Profit;  FORMAT DateReturned DATE9. Profit DOLLAR6.2; |\

\
\

可以先設置好模版，之後調用。由數值，帶換成文字標題。

|  |
| --- |
| **PROC****FORMAT**; VALUE  **S07FMT**  **1**='總計　　　　　'  **2**='農耕業　　　　　' |\

\
|\
 **PROC****PRINT**DATA=--- label noobs split='/';  VAR    st ---;  FORMAT   st  **S07FMT.**;  LABEL    st='主要經營/種類';  run; |\

\
\

模式1：summary

可以加總列資料。

|  |
| --- |
| **PROC****SUMMARY**DATA=T01; CLASS AREA; VAR COL8 - COL17; OUTPUT OUT=T02  SUM=SCOL8-SCOL17  MEAN= SCOL8-SCOL17; |

模式2：means

可以列出最大值（列資料，不是行變量）、最小值、平均值、中位数、標準差、總和等等。

|  |
| --- |
| **proc****MEANS**DATA=zn02; class hs; var col1; OUTPUT OUT=zn03  SUM= col1; |

如果加上”SUM”的話，會有兩個表，一個是列出統計資料的結果表，另一個是包含變量按階層的加總總和的資料集。

前二模式基本差異見這裡：<http://www.amadeus.co.uk/sas-technical-services/tips-and-techniques/general/basic-differences-between-proc-means-and-proc-summary/>

模式二該知道的本質：<http://www2.sas.com/proceedings/sugi26/p064-26.pdf>

模式三：freq

計算次數。

|  |
| --- |
| **proc****freq**DATA=hs07; where hs='65'; TABLES distno; **run**; |

TABLES 決定怎麼數數兒，如 var1，var1 \* var2 等。

Where 決定子集合。

模式四：tabulate

使用博主資料，希望我也能有一艘遊艇。

|  |
| --- |
| CSV資料 Silent Lady,Maalea,sail,sch,75,153  America II,Maalea,sail,yac,32.95,125  Aloha Anai,Lahaina,sail,cat,62,117  Ocean Spirit,Maalea,power,cat,22,162  Anuenue,Maalea,sail,sch,47.5,111  Hana Lei,Maalea,power,cat,28.99,115  Leilani,Maalea,power,yac,19.99,119  Kalakaua,Maalea,power,cat,29.5,134  Reef Runner,Lahaina,power,yac,29.95,126  Blue Dolphin,Maalea,sail,cat,42.95,124 |\

\
|\
 **DATA** boats; INFILE 'c:\MyRawData\Boats.csv' DLM =','DSD MISSOVER;  INPUT Name:$13.  Port:$7.  Locomotion:$5.  Type:$3.  Price;  RUN;  /\* Tabulations with three dimensions; \*/  **PROC****TABULATE**DATA = boats;  CLASS Port Locomotion Type;  TABLE Port, Locomotion, Type;  TITLE 'Number of Boats by Port, Locomotion, and Type';  **RUN**; |\

\
|\
 /\* PROC TABULATE report with options; \*/ **PROC****TABULATE**DATA = boats FORMAT=DOLLAR9.2;  CLASS Locomotion Type;  VAR Price;  TABLE Locomotion ALL, MEAN \* Price \* (Type ALL)  /BOX='Full Day Excursions' MISSTEXT='none';  TITLE;  **RUN**; |\

\
|\
 /\* Using the FORMAT= option in the TABLE statement; \*/ **PROC****TABULATE**DATA = boats;  CLASS Locomotion Type;  VAR Price Length;  TABLE Locomotion ALL,  MEAN \* (Price \* FORMAT=DOLLAR6.2  Length \* FORMAT=**6.0**) \* (Type ALL);  TITLE 'Price and Length by Type of Boat';  **RUN**; |\

\
\

SAS讀CSV檔時，若遇文字格式，需要提示：”:$\*. ”。

/BOX 左上角的方格標籤

VAR 無，給個數；有，it depends。這是行變量，無庸置疑放表頭。

TABLE這是列變量，無庸置疑放表側。

FORMAT 修飾格式，本例加入金錢符號 $。

模式五：report

可以畫出相當漂亮的表，不過我還在測試中。但，可以將表匯入資料集中，以data階段或proc階段繼續烹調。

|  |
| --- |
| /\* Statistics in COLUMN statement with two group variables; \*/ **PROC****REPORT**DATA = boats  NOWD HEADLINE;  COLUMN Locomotion Port N (Price Length),MEAN;  DEFINE Locomotion / GROUP;  DEFINE Port / GROUP;  TITLE 'Statistics with Two Group Variables';  **RUN**;  /\* Statistics in COLUMN statement with group and across variables; \*/  **PROC****REPORT**DATA = boats NOWD HEADLINE;  COLUMN Locomotion N Port,(Price Length),MEAN;  DEFINE Locomotion / GROUP;  DEFINE Port / ACROSS;  TITLE 'Statistics with a Group and Across Variable';  **RUN**; |\

\
\
