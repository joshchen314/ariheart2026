---
categories:
- SAS
- SAS 101
date: '2014-04-25T03:24:59+08:00'
draft: false
slug: sas-101-day-6-巨集
tags: []
title: SAS 101 Day 6 巨集
---

1. **概念**

一開始，我以為 SAS 巨集的概念和 R 的函數（function）只是很像而已。其實，**SAS****的巨集就是****R****的函數**（自定義的）如下：\

|  |
| --- |
| 1. SAS  %macro ***h11*** (startnum,stopnum)         /\* 定義一個巨集\*/ %DO N = &startnum %TO &stopnum … %END; %MEND H11;                         /\* 結束定義\*/ %***h11***(**1**,**15**);  /\*使用定義好的巨集\*/  %***h11***(**12**,**51**);    2. R     ***h11*** <-- function(startnum, stopnum) {     /\* 定義一個函數\*/     ***…***}                                   /\* 結束定義\*/     ***h11***(**1**,**15**)     ***h11***(**12**,**51**) |\

\
\

概念真的很簡單，操作起來就不一定了，有可能會非常複雜，甚至有專門的偵錯工具，如SYMBOLGEN，etc。至少，有一個原則就是，絕對把DATA階段與PROC階段分的一清二楚，尤其是加上條件語句（ IF … THEN DO;…;END; ELSE DO;…;END;）。因為，在巨集裏面，DATA階段與PROC階段沒有顏色區分，很容易混淆。

若說 DATA階段是山， PROC階段是海，那麼巨集就能包山包海了。

對我而言，第一次做巨集程式，既緊張又興奮，洋洋灑灑寫完，結果跑不出來。仔細一看，原來是用條件語具把DATA階段與PROC階段混在一起了。來個CASE STUDY，細節如下：

|  |
| --- |
| %macro ***h11*** (startnum,stopnum) %DO **N** = &startnum %TO &stopnum  /\* 這個非常關鍵，命名為 **N** \*/ **data T01;**if **0**<**&N**<**10** then do;               /\* 這個非常關鍵， **&N** 調用 \*/ **PROC SUMMARY DATA=T01;**run; end; else do; PROC SUMMARY DATA=T01; run; end; run; %END; %MEND H11; |

我的錯誤就是用DATA階段包一個條件語句，再用條件語句包一個PROC階段。明顯低級錯誤，居然用DATA階段包一個PROC階段，而且DATA階段也沒有讀資料檔的動作。所以，把那哥倆好分開之後，料理就出爐了。

|  |
| --- |
| %macro ***h11*** (startnum,stopnum) %DO **N** = &startnum %TO &stopnum  /\* 這個非常關鍵，命名為 **N** \*/ **data T02 T03;****set T01;**if **0**<**&N**<**10** then output T02;               /\* 這個非常關鍵， **&N** 調用 \*/ else if 10<=**&N** then output T03; **PROC SUMMARY DATA**=T02**; var** stha**;****OUTPUT OUT**=T02S**SUM**=stha; run;**PROC SUMMARY DATA**=T03**; var** stha**;****OUTPUT OUT**=T03S**SUM**=stha; run; %END; %MEND H11; |

NOTE:

1. D0801**2**, D0802**2**, D0803**2**, D0804**2**, D0805**2**, …, D0899**2**  巨集的方便就是可以批次的、按規則的料理行變數。上面的數列若要用PROC階段加總，可能會需要99+個。
   透過巨集，使用 “&N” 標籤，用 ”D08&N . **2**” 表達就可以達成目的。

溫馨提示一，“&N” 標籤需要一個 “ . “ 來與 **2**隔開，像這樣，D08&N**.2****。**

溫馨提示二，巨集裡的數字是表示成”文字”，不是”值”。所以，N 的範圍要從 01 至 99，那數列在 1 至 9 的範圍就不會少一個 “0”。

Reference:

1. <http://www.loyhome.com/learning-sas-in-7-days-6/>
2. <http://r97846001.blog.ntu.edu.tw/2011/01/13/sas-macro-%E5%8F%8D%E8%A6%86%E9%81%8B%E7%AE%97do-part1/>
3. <http://carllin76.blogspot.tw/2008/11/sas-macro.html>

**2.** **分解動作**

其實，**SAS****的巨集就是R****的函數**（自定義的）。一面來講，望文生義，巨集就是一個**自己**為經常重複**而預先定義**好的運算單元。比如說，我在整理資料後，經常使用 PROC SUMMARY 把資料加總後生成新的資料集。如果依照行變數可以有 5 種資料整理的方式，這 5 種要用 PROC SUMMARY 加總，並分別生成 5 張資料集。也就是說：

|  |
| --- |
| DATA …; PROC SUMMARY …; CLASS AREA; VAR COL1-COL5; OUTPUT OUT=A1\_1 SUM=…;DATA …; PROC SUMMARY …; CLASS AREA; VAR COL1-COL5; OUTPUT OUT=A2\_3 SUM=…;DATA …; PROC SUMMARY …; CLASS AREA; VAR COL21-COL25; OUTPUT OUT=A3\_5 SUM=…;DATA …; PROC SUMMARY …; CLASS BIRTH; VAR COL1-COL5; OUTPUT OUT=A4\_1 SUM=…;DATA …; PROC SUMMARY …; CLASS BIRTH; VAR COL6-COL10; OUTPUT OUT=A5\_2 SUM=…; |

但是，使用 巨集，一切就變得很簡潔：

|  |
| --- |
| %MACRO A1(M, N, O, P) PROC SUMMARY …; CLASS AREA; VAR COL&M-COL&N OUTPUT OUT=A&O.\_&P SUM=…;%MACRO A2(M, N, O, P) PROC SUMMARY …; CLASS BIRTH; VAR COL&M-COL&N OUTPUT OUT=A&O.\_&P SUM=…;DATA …; %A1(1,5,1,1);DATA …; %A1(1,5,2,3)DATA …; %A1(21,25,3,5)DATA …; %A2(1,5,4,1) DATA …;  %A2(6,10,5,2) |\

\
\

上面只重複 5 次而已，差異沒那麼明顯。但是，若需要 40 組 PROC SUMMARY，那麼差異就會非常顯著了！

也就是說，我把 巨集 A1 與 巨集 A2 預先設定為 列印巨集1 與列印巨集2，下一次我要使用時，就可以直接調用，並把參數丟進去，就能得到自己要的結果。

**3. CASE STUDY**

|  |
| --- |
| **data** T01; set T01; **%MACRO** H09(startnum,stopnum); %DO I=&startnum %TO &stopnum %LET J=%EVAL(2\*(&I-1)+101);      /\* 巨集內的函數運算 \*/ %LET K=%EVAL(2\*(&I-1)+102);      /\* 巨集內的函數運算 \*/ IF **1**<=&i<=**9** then do; IF D7&0i>**0** THEN COL&J=**1**;ELSE COL&J=**0**; COL&K=D70&i    end; else do; IF D7&i>**0** THEN COL&J=**1**;ELSE COL&J=**0**; COL&K=D07&i    end; %END; **%MEND** H09; %***h09***(**1**,**30**); IF D731>**0**THEN COL161=**1**;ELSE COL161=**0**; IF D731=**0**THEN COL162=**1**;ELSE COL162=**0**; /\*------------------------------------------\*/ %***A1***(**101**,**161**,**09**,**1**); %***A2***(**101**,**161**,**09**,**2**); |

note:\
本例中，code不完美，因為會出現遺漏值。原因出在 IF-THEN-ELSE條件語句，應該要改成：\
%IF **1**<=&i<=**9** %then %do; ...; %end;

%IF **10**<=&i<=**99** %then %do; ....; %end;\
〈2014.7.27 更新。其中有很多奧妙之處，還要再研究研究。〉

**%LET J=%EVAL(2\*(&I-1)+101)**

這邊要說明的概念，是如何用一個循環變數（I）影響多個變數（J, K）一起”循環”。這裡有一個觀念，巨集語言把所有的”數字”都當作”文字”，並不是”值”，所以不能直接進行數學運算。所以，在巨集裡，” J = 2\*(&I-1)” 是有問題的。因此，要先以 “&LET” 先產生一個新的變數 “J”，之後才能以“&J”調用，並且，要以 ”%EVAL( )” 帶進整數的函數運算，作值的加減乘除。

小發現：用” %***h09***(**1**,**30**)” 調用巨集後，雖然 1 至 30 是數字，但送進迴圈後會按”**值**”做遞進。也就是說，” %***h09***(**01**,**30**)”的數字送進 “%DO I=&startnum %TO &stopnum” 迴圈後，01至09就會成為 1 至 9 。因此，上面例子就以條件語句判斷 N 為 1 至 9 ，則加一個 ”0”。

%***A1***(**101**,**161**,**09**,**1**);

按前例，是一個列印巨集，這裡”**09**”沒有進迴圈，所以，直接是以”**文字表達**”，不用擔心是否補 ”0”。
