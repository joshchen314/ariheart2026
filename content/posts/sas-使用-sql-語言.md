---
categories:
- SAS
- SAS 101
date: '2014-08-08T03:46:39+08:00'
draft: false
slug: sas-使用-sql-語言
tags: []
title: SAS 使用 SQL 語言
---

SQL 是結構化查詢語言（ [STRUCTURED QUERY LANGUAGE](http://en.wikipedia.org/wiki/SQL)），這是根據 WIKI。為何需要在 SAS 裏面使用 SQL 語言呢？因為在 SAS  跑完資料後，我會想要驗證結果是否正確。雖然使用 DATA 階段配合 DROP 與 KEEP 也可以達到類似的目的。但是，若是使用 SQL 語法，對我來說，有兩個便利的地方，第一， SQL 更有彈性，第二，方便管理，我只要讀到 SQL 的部分，就知道是作結果驗證。首先，先來看看，SQL 與 SAS 的資料結構（來自[這裡](http://r97846001.blog.ntu.edu.tw/2010/09/26/procsqlintro/)）：
SQL table = SAS data file
SQL column = variables
SQL row = obs IN SAS data file
第二，架構是，紅色字體是必要的部分：
**PROC SQL;**
**SELECT**        ---------->**選擇** 哪些欄位（變數）作查詢 
 **FROM               ---------->****來自**哪張 TABLE    
WHERE        ---------->**條件語句**可以放在這裡
GROUP BY
HAVING
ORDERED BY
**;                                  ---------->**這絕對要加上去
**QUIT;**
([這裡](http://r97846001.blog.ntu.edu.tw/2011/09/15/dear-miss-sasanswers/) 有每一項的明確解釋) ([連結1](http://r97846001.blog.ntu.edu.tw/2010/09/27/sas-sql-%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9/))([連結2](http://r97846001.blog.ntu.edu.tw/2010/09/29/sassqlpart2/))([連結3](http://r97846001.blog.ntu.edu.tw/2010/10/01/sas-sql-%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4%E4%BB%8B%E7%B4%B9part3/))
 
第三，如果使用 SAS ENTERPRISE GUIDE 的話，可以選擇 完全 不要寫語法，用點選的就可以完成了。很明顯，我在驗證結果的時候，真的是懶洋洋的，不想寫語法。所以， SQL 成為我的最愛之一。
SAS EG 的點選流程可以參考這裡的投影片（[連結](https://ariheart2011.wordpress.com/wp-admin/post-new.php)）。
 
第四，用個例子比較一下：
（1）直接用 SAS DAT STEP：
data A102\_2;
SET A102\_1;
if A091002='1' then output; else delete;
KEEP A000000 A091002 A092001 A060001 A121101 A122201;
（2）用 SQL ：
PROC SQL;
create table A102\_2 as
SELECT A000000, A091002, A092001, A060001, A121101, A122201   /\* **逗號**分隔 \*/
FROM A102\_1
where A091002='1'
;
QUIT;
（3）條件語句
PROC SQL;
create table kk1\_tea as
SELECT \*
FROM HUSALL
**where DD contains 'ART'        /\* 抓出 DD 含有 "ART" 的樣本 \*/**
;
QUIT;
小結：作為使用者， SAS DATA STEP 當然是要做啥都可以，包山包海，但有時想換種口味，就會用更強調查詢功能的 SQL 語言，更為直覺，比如說 SELECT，把 A000000 等變數"選擇"拿出來，並且，在 A091002='1' 時回傳資料來。
 
**結論：**
最重要的，請記得 " ; " 該擺在哪裡，SQL 與 SAS STEP 不太一樣，不用每一行都添加，需要特別留意。並且 SELECT 變數時，需要以 " , " 分隔。
That's all. Happy Friday night!
