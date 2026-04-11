---
categories:
- 統計地圖
- SAS
date: '2017-05-09T17:00:08+08:00'
draft: false
slug: 深入淺出繪製統計地圖-2-sas
tags: []
title: 深入淺出繪製統計地圖 2 - SAS
---

如同曹植的七步成詩，我們要來「三步畫統計地圖」，這樣才能深入淺出繪製出迷人的統計地圖。這一篇筆記是要說明，如何以 SAS EG 繪製美麗的統計地圖。雖然使用程式碼，但是基本的架構很清晰，就是**先分別匯入圖資檔與統計資料**檔，並確保二者有一個共同鍵值，如COUNTYNAME，然後，**使用SAS的Graph模組，以proc gmap方法進行繪製作業**，就可以獲得美麗的地圖。

這一篇筆記的運作方式，是將程式碼都呈現出來，可以直接在SAS上執行，必需要修改的部分已經加上藍色標記，比如說匯入圖資檔與統計資料檔的檔案路徑，或是統計資料檔的哪一個變數。下圖是依據104年農林漁牧業普查之農事及畜牧服務業資料繪製的。

![sas gmap 2](../../images/2017/sas-gmap-2.png)

**第一步，先匯入shp圖資檔**（已經轉成big5格式），資料包含到縣市的鄉鎮市區級資料，資料檔的欄位名稱為COUNTYNAME, COUNTYID, COUNTYCODE, TOWNNAME, TOWNID, TOWNCODE。再以**PROC** **GREMOVE方法，將鄉鎮市區的界線抹掉，以得到縣市級的階層；這是為了保有彈性，使得我們能夠產製縣市級、鄉鎮市區級的地圖，但是，如使用縣市級、村里級或是非內政部國土測繪中心（2015/12）的圖資檔，就需要修改紫色標記。如果需要幫地圖別上縣市名稱的標籤，可以使用內建的巨集，%*annomac***與**%*maplabel***方法。

**這個步驟可以得到圖資檔WORK.SORTSortedVILLAGEMAP，以及標籤檔maplabel**。

**/\*\* --   第 1 步讀取 shp 程式：圖資檔   -- **/\
proc** **mapimport** out=VILLAGEMAP datafile="＊＊\SASMAP\TOWN20161214.SHP";\
 SELECT COUNTYNAME COUNTYID COUNTYCODE TOWNNAME TOWNID TOWNCODE ;    **RUN**;\
**PROC** **SORT** DATA= VILLAGEMAP OUT= TOWNMAP;    BY COUNTYCODE;    **RUN**;\
**PROC** **GREMOVE** DATA = TOWNMAP OUT =TOWNMAP;\
BY COUNTYCODE NOTSORTED COUNTYNAME;\
 ID TOWNCODE ;  **RUN**;\
%***\_eg\_conditional\_dropds***(WORK.SORTSortedVILLAGEMAP);\
**PROC** **SORT** DATA=WORK.VILLAGEMAP\
OUT=WORK.SORTSortedVILLAGEMAP(LABEL="已排序 WORK.VILLAGEMAP") NODUPKEY;\
BY COUNTYCODE COUNTYID COUNTYNAME;**RUN**;**RUN**; **QUIT**;TITLE; FOOTNOTE;\
**proc** **sort** data=townmap;       by COUNTYNAME;     **run**;\
%***annomac***;\
%***maplabel*** (townmap,townmap, maplabel,COUNTYNAME,COUNTYNAME,font=標楷體, color=black, size=**2**, hsys=**3**);\
**run**;\
/** --   讀取 shp 程式：圖資檔 程序結尾。   -- \*\*/

**第二步就是匯入統計資料檔**，並設定資料的級距。這個步驟獲得的統計資料檔是INCOME2。

/\*\* --   C.1. 第 2 步先匯入資料集：『讀取新資料檔請務必修改』   -- **/\
LIBNAME KIT '＊＊＊＊＊＊\SASMAP\';\
**PROC** **IMPORT** OUT= INCOME2\
DATAFILE= "＊＊＊＊＊＊\SASMAP\agr.csv"\
DBMS=CSV REPLACE;\
GETNAMES=YES;**run**;\
/** --   讀取 資料檔 程序結尾。   -- \*\*/

**第三步就是把前二者整合在一起**，方法是 PROC GMAP，而『CHORO』後就是需要繪製出的 統計量，這裏是用變數FSN。

然後，對4個參數進行微調，並且圖例（Legend）也會相應調整；**設定級距**（2個地方；因為系統自訂的為不連續）， **設定級距數**（2個地方，這裡的例子是用4個級距），**設定圖例名稱**（1個地方），**設定顏色**（1個地方）；或者直接修改我有標記註解的地方。

關於「DEVICE=PNG」功能，這是因為系統預設的統計地圖檔案格式為ActiveX，雖然可以互動，但是在繪製進行匯出作業（其實是複製、貼上）來講不方便，生成PNG檔就比較好處理。

/\*\* --   第 3 步執行地圖圖表程式碼   -- **/\
/** --    D.1. 先設定級距     -- **/\
**proc** **format**;\
value AGR4\_N low-**100**  = 'Up to 100'\
**101**-**250**  = '101 - 250'\
**251**-**400**  = '251 - 400'\
**401**-high  = 'Over 400';**run**;\
/** --    D.1. 設定級距     -- **/\
%***\_eg\_conditional\_dropds***(WORK.MAPCHARTMAPPREP);\
**PROC** **SQL**;   CREATE VIEW WORK.MAPCHARTMAPPREP AS\
SELECT \*               FROM WORK.TOWNMAP         ;**QUIT**;\
%***\_eg\_conditional\_dropds***(WORK.MAPCHARTRESPONSEPREP);\
**PROC** **SQL**;   CREATE VIEW WORK.MAPCHARTRESPONSEPREP AS\
SELECT \*               FROM WORK.INCOME2;**QUIT**;\
%***\_sas\_pushchartsize***(**1500**, **1200**);               GOPTIONS /** DEVICE=PNG **/  CBACK=  ;\
/**    D.4. 設定顏色    **/\
PATTERN1 VALUE=SOLID COLOR=VPAP;\
PATTERN2 VALUE=SOLID COLOR=LIP;\
PATTERN3 VALUE=SOLID COLOR=BIP;\
PATTERN4 VALUE=SOLID COLOR=VIP;/**    圖例    **/\
LEGEND1\
DOWN=**4**    /**    D.2. 設定級距數    **/\
FRAME\
POSITION=(BOTTOM LEFT OUTSIDE)\
LABEL=(FONT='標楷體' HEIGHT=**9**pt JUSTIFY=LEFT "家數");   /**   D.3. 設定圖例名稱  **/\
TITLE;FOOTNOTE;\
TITLE1 "104年農林漁牧業普查-統計地圖";\
FOOTNOTE1 "由 SAS 系統 (&\_SASSERVERNAME, &SYSSCPL) 於 %TRIM(%QSYSFUNC(DATE(), NLDATE20.))%TRIM(%SYSFUNC(TIME(), NLTIMAP16.)) 產生";\
**PROC** **GMAP** GOUT=MAPCHART DATA=WORK.MAPCHARTRESPONSEPREP MAP=WORK.MAPCHARTMAPPREP ALL ;\
FORMAT FSN AGR4\_N.;    /**    D.1. 設定級距    **/\
ID COUNTYNAME;\
CHORO FSN /            /**   C.2. 『讀取新資料檔請務必修改』：將 FSN 改成需要的 統計量  **/\
discrete\
WOUTLINE=**1\**                LEVELS=**4**                     /**    D.2. 設定級距數    **/\
STATISTIC=SUM\
LEGEND=LEGEND1\
ANNOTATE=MAPLABEL;         /**    呼叫標籤檔    **/\
**RUN**;**QUIT**;TITLE;FOOTNOTE;GOPTIONS RESET=LEGEND; %***\_sas\_pushchartsize***;GOPTIONS CBACK=;\
%***\_eg\_conditional\_dropds***(WORK.MAPCHARTRESPONSEPREP);\
%***\_eg\_conditional\_dropds***(WORK.MAPCHARTMAPPREP);\
/** --   工作程式碼結尾   -- \*\*/

結論：\
用SAS來繪製統計地圖，比我想像的容易許多，也想再多研究一些。所以，我發現還能在統計地圖上增加一個統計量，甚至是使用R來繪製統計地圖，我們之後繼續討論。或者，有不盡善盡美的地方，請直接聯絡作者，email: sandalphu@gmail.com 或 josh314@dgbas.gov.tw。

![SAS map](../../images/2017/sas-map.png)

![Rplot2](../../images/2017/rplot2.png)

附錄：COLOR LIST： COLOR=前綴縮寫+顏色縮寫----> VPAP= VPA + P。

|  |  |
| --- | --- |
| 前綴 | 縮寫 |
| pale | PA |
| brilliant | BI |
| light | LI |
| moderate | MO |
| medium | ME |
| strong | ST |
| dark | DA |
| deep | DE |
| vivid | VI |
| very pale | VPA |
| very light | VLI |
| very dark | VDA |
| very deep | VDE |

|  |  |
| --- | --- |
| 顏色 | 縮寫 |
| red | R |
| pink | PK |
| olive | OL |
| brown | BR |
| orange | O |
| yellow | Y |
| yellow-green | LG |
| yellowish green | YG |
| green | G |
| blue | B |
| purple | P |
| violet | V |
| gray | GR |
| black | BL |
| white | WH |
