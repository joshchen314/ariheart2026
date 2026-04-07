---
categories:
- SAS
date: '2018-07-17T09:12:25+08:00'
draft: false
slug: ods、excel與文字格式：first-與-call-define
tags: []
title: ODS、EXCEL與文字格式：FIRST 與 CALL DEFINE
---

在進行資料處理時，經常會運用「鄉鎮村里檔」，格式通常都是縣市、鄉鎮、村里、代碼等的欄位格式。如下：

|  |
| --- |
| 6301002 臺北市松山區　莊敬里6301003 臺北市松山區　東榮里 6301004 臺北市松山區　三民里 6301005 臺北市松山區　新益里 6301006 臺北市松山區　富錦里 6301007 臺北市松山區　新東里 |

但是，如果需要產生成印刷版，會希望是階層式的，以便於閱讀，如下：

|  |
| --- |
| **臺北市　(63)****松山區****(01)** 莊敬里　　　002 東榮里　　　003 三民里　　　004 新益里　　　005 富錦里　　　006 新東里　　　007 |

作法當然有兩種，一種很直接，就是用複製、貼上、改字體格式，另一種就是用程式產生。這兩種我都用過，前者是剛進機關，什麼也不懂，只懂複製、貼上、改字體格式；現在的話，我就用SAS軟體。
SAS軟體的功能，想法上是以 **DATA方法**之「FIRST」讀取資料，並以**PROC REPORT** **方法**之「CALL DEFINE」設定條件以改字體格式。這樣就能得到階層化的全國鄉鎮村里檔，可以用ODS匯出成RTF或是EXCEL；不僅如此，ODS方法配合巨集方法，可以進一步將22個縣市的村里檔劃分成EXCEL的22個頁籤，這樣閱讀、使用起來更方便。
ODS方法配合巨集方法之程式碼如下：
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/
FILENAME indATA ‘\Saseg\D54\d54b\0\_DATA\名冊\A10420171222.txt’;
DATA AGRNOC104;
INFILE indATA LRECL=32 DSD MISSOVER END=eof;
INPUT
@1 CODE $7.
@1 HSCODE $2.
@3 CNTCODE $2.
@5 TNCODE $3.
@9 HSNAME $CHAR6.
@15 CNTNAME $CHAR8.
@23 TOWNAME $CHAR8.;
RUN;
DATA AGRNOC104A;
SET AGRNOC104; BY HSCODE CNTCODE TNCODE;
**IF FIRST.HSCODE THEN OUTPUT;**
**IF FIRST.CNTCODE THEN OUTPUT;** RUN;
DATA AGRNOC104B;
SET AGRNOC104; BY HSCODE CNTCODE TNCODE;
COM1=”(“; COM2=”)”;COM3=”　”; COM4=”　”;COM5=”　　”;
IF FIRST.HSCODE THEN DO;
**LN=1;**
NAMET=catt(OF HSNAME COM3);
CODET=catt(OF COM1 HSCODE COM2) ;
OUTPUT;
END;
IF FIRST.CNTCODE THEN DO;
**LN=2;**
NAMET=catt(OF CNTNAME COM4);
CODET=catt(OF COM1 CNTCODE COM2) ;
OUTPUT;
END;
IF FIRST.TNCODE THEN DO;
**LN=3;**
NAMET=catt(OF TOWNAME COM5);
CODET= TNCODE ;
OUTPUT;
END;
RUN;
DATA AGRNOC104C(KEEP=LN HSCODE NAMEF);
SET AGRNOC104B;
NAMEF=catt(OF NAMET CODET) ;
RUN;
**%MACRO makeHS(HSN);**
**ods tagsets.excelxp options(sheet\_name=”HS&HSN”) ;**
proc report data=AGRNOC104C ;
WHERE HSCODE=”&HSN”;
column LN NAMEF ;
define LN / display;
define NAMEF / display;
compute LN;
if LN = 1 then**call define**(*row*,”style”,”style={fontfamily=’Times New Roman’ fontsize=14PT font\_weight=bold}”);
if LN = 2 then **call define**(*row*,”style”,”style={fontfamily=’Times New Roman’ fontsize=10PT font\_weight=bold}”);
if LN = 3 then **call define**(*row*,”style”,”style={fontfamily=’Times New Roman’ fontsize=8PT}”);
endcomp;
run;
**%MEND;**
**ods** tagsets.excelxp body=’\Saseg\D54\d54b\AGRNOC104C.XLS’;
%makeHS(63);%makeHS(64);%makeHS(65);%makeHS(66);%makeHS(67);%makeHS(68);
%makeHS(02);%makeHS(04);%makeHS(05);%makeHS(07);%makeHS(08);%makeHS(09);
%makeHS(10);%makeHS(13);%makeHS(14);%makeHS(15);%makeHS(16);%makeHS(17);
%makeHS(18);%makeHS(20);
%makeHS(71);%makeHS(72);
**ods** tagsets.excelxp close;
/\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*//\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*/
