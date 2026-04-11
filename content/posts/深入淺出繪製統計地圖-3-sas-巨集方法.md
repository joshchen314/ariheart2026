---
categories:
- 統計地圖
- SAS
date: '2017-05-10T03:28:56+08:00'
draft: false
slug: 深入淺出繪製統計地圖-3-sas-巨集方法
tags: []
title: 深入淺出繪製統計地圖 3 - SAS 巨集方法
---

SAS 巨集方法其實就是 R語言的 Function方法，[非常方便](https://goo.gl/a5x4RJ)。這一篇筆記就直接呈現巨集的程式碼，細部調整就參考 [這一篇](https://goo.gl/V6DJQ9)。

/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\
\* 目的： 快速畫出統計地圖，作為分析前的預備動作，再挑選有興趣的主題，並微調細部參數\
\* 圖資檔： 內政部國土測繪中心的鄉鎮市區級圖資檔（105/12/14），已轉Big5格式\
\* 參考網址：https://goo.gl/V6DJQ9 ==>提供進一步微調細部參數的解釋\
\* 作者：陳弦業；josh314@dgbas.gov.tw\
\* 操作說明：\
\* 第一步，使用 gisMap 巨集：這是用來匯入圖資檔的，只需要執行一次\
\* 第二步，使用 MapTW 巨集：\
\*\* 1. PATH\_VAR：統計資料檔所在路徑\
\*\* 2. TTLE：為地圖取個名字吧！\
\*\* 3. ST： 統計量\
\*\* 4. LVD： 統計量的級距數\
\*\* 5. UE： 統計量的單位\
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/

%MACRO gisMap(MAP\_VAR);\
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\
\*\*\* macro 參數: 0. MAP\_VAR：圖資檔所在路徑\
\*\*\* 只需要執行一次 \*\*\* 只需要執行一次 \*\*\* 只需要執行一次\*\*\*\
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/\
proc mapimport out=VILLAGEMAP datafile="&MAP\_VAR.";/\*\* -- 第 1 步讀取 shp 程式：圖資檔 -- \*\*/\
SELECT COUNTYNAME COUNTYID COUNTYCODE TOWNNAME TOWNID TOWNCODE ; RUN;\
PROC SORT DATA= VILLAGEMAP OUT= TOWNMAP; BY COUNTYCODE; RUN;\
PROC GREMOVE DATA = TOWNMAP OUT =TOWNMAP;\
BY COUNTYCODE NOTSORTED COUNTYNAME;\
ID TOWNCODE ; RUN;\
%\_eg\_conditional\_dropds(WORK.SORTSortedVILLAGEMAP);\
PROC SORT DATA=WORK.VILLAGEMAP\
OUT=WORK.SORTSortedVILLAGEMAP(LABEL="已排序 WORK.VILLAGEMAP") NODUPKEY;\
BY COUNTYCODE COUNTYID COUNTYNAME;RUN;RUN; QUIT;TITLE; FOOTNOTE;\
proc sort data=townmap; by COUNTYNAME; run;\
%annomac;\
%maplabel (townmap,townmap, maplabel,COUNTYNAME,COUNTYNAME,font=標楷體, color=black, size=2, hsys=3);\
run;\
%MEND gisMap;\
%gisMap(＊＊＊\SASMAP\TOWN20161214.SHP); /\*\*\* 只需要執行一次 \*\*\* 只需要執行一次 \*\*\* 只需要執行一次\*\*\*/

%MACRO MapTW(PATH\_VAR,TTLE,ST,LVD,UE);\
PROC IMPORT OUT= INCOME2/\*\* -- C.1. 第 2 步先匯入資料集 -- **/\
DATAFILE= "&PATH\_VAR."\
DBMS=CSV REPLACE;\
GETNAMES=YES;run;\
%\_eg\_conditional\_dropds(WORK.MAPCHARTMAPPREP);/** -- 第 3 步執行地圖圖表程式碼 -- **/\
PROC SQL; CREATE VIEW WORK.MAPCHARTMAPPREP AS\
SELECT \* FROM WORK.TOWNMAP ;QUIT;\
%\_eg\_conditional\_dropds(WORK.MAPCHARTRESPONSEPREP);\
PROC SQL; CREATE VIEW WORK.MAPCHARTRESPONSEPREP AS\
SELECT \* FROM WORK.INCOME2;QUIT;\
%\_sas\_pushchartsize(1500, 1200); GOPTIONS DEVICE=PNG CBACK= ;\
PATTERN1 VALUE=SOLID COLOR=VPAP;/** D.4. 設定顏色 **/\
PATTERN2 VALUE=SOLID COLOR=LIP;\
PATTERN3 VALUE=SOLID COLOR=BIP;\
PATTERN4 VALUE=SOLID COLOR=VIP;\
LEGEND1/** 圖例 **/\
DOWN=&LVD /** D.2. 設定級距數 **/ FRAME POSITION=(BOTTOM LEFT OUTSIDE)\
LABEL=(FONT='標楷體' HEIGHT=9pt JUSTIFY=LEFT &UE); /** D.3. 設定圖例名稱 **/\
TITLE;FOOTNOTE;\
TITLE1 "&TTLE.";\
FOOTNOTE1 "由 SAS 系統 (&\_SASSERVERNAME, &SYSSCPL) 於 %TRIM(%QSYSFUNC(DATE(), NLDATE20.))%TRIM(%SYSFUNC(TIME(), NLTIMAP16.)) 產生";\
PROC GMAP GOUT=MAPCHART DATA=WORK.MAPCHARTRESPONSEPREP MAP=WORK.MAPCHARTMAPPREP ALL ;\
ID COUNTYNAME;\
CHORO &ST / /** C.2. 『讀取新資料檔請務必修改』：將 FSN 改成需要的 統計量 **/\
WOUTLINE=1\
LEVELS=&LVD /** D.2. 設定級距數 **/\
STATISTIC=SUM\
LEGEND=LEGEND1\
ANNOTATE=MAPLABEL; /** 呼叫標籤檔 \*\*/\
RUN;QUIT;TITLE;FOOTNOTE;GOPTIONS RESET=LEGEND; %\_sas\_pushchartsize;GOPTIONS CBACK=;\
%\_eg\_conditional\_dropds(WORK.MAPCHARTRESPONSEPREP);\
%\_eg\_conditional\_dropds(WORK.MAPCHARTMAPPREP);\
%MEND MapTW;

%MapTW(＊＊＊\SASMAP\agr.csv, 104年農林漁牧業普查統計地圖-農牧戶, FHN, 6, "農牧戶家數");\
%MapTW＊＊＊\SASMAP\agr.csv, 104年農林漁牧業普查統計地圖-農牧場, FMN, 3, "農牧場家數");\
%MapTW(＊＊＊\SASMAP\agr.csv, 104年農林漁牧業普查統計地圖-農事服務業, FSN, 4, "農事服務業家數");\
%MapTW(＊＊＊\SASMAP\agr.csv, 104年農林漁牧業普查統計地圖-林業, FORN, 5, "林業家數");\
%MapTW(＊＊＊\SASMAP\agr.csv, 104年農林漁牧業普查統計地圖-漁業, FISHN, 5, "漁業家數");

[gallery ids="626,625,624,623,622" type="rectangular"]
