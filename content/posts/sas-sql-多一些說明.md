---
categories: []
date: '2015-02-14T00:30:04+08:00'
draft: false
slug: sas-sql：多一些說明
tags: []
title: SAS SQL：多一些說明
---

我之前已經整理過 SAS SQL 的筆記，記錄基礎且簡單的語法，如 select, where, contain。這裡有更完整的介紹（<http://sugiclub.blogspot.tw/2007/02/introduction-to-sql-in-sas.html>）。
那一篇博文可以簡單分做三個部分：基本語法、條件語法、統計運算。這一篇會先記錄關於後兩者的部分。

1. 條件語法

（<http://www.1keydata.com/tw/sql/sql-case.html>）
CASE 是 SQL 的 IF-THEN-ELSE關鍵字，所以，在 SAS 也不例外。
/*---*/

|  |  |
| --- | --- |
| **SELECT CASE WHEN "****欄位名" "****條件1" THEN "****結果1" ... [ELSE "****結果N"] END FROM "****表格名";** | **PROC** **SQL**; create table kk777\_tea as SELECT CASE WHEN  D010001 EQ **6** THEN **1**ELSE **0**END AS ChkThese FROM HUSALL ; **QUIT**; |

/*---*/
如果只挑出有 missing data 的變數，用 is null 或 is missing ：
/*---*/
select   from **"****表格名"**where **"****變數"** is null;
/*---*/

2. 統計運算

/*---*/   清單   /*---*/
Sum：總和
Max ：最大值
Min ：最小值
Avg：平均數
Var：變異數
Std：標準差standard deviation
NMiss： missing values 的個數
Count：non-missing values 的個數
/*---*/
/*---*/ 例子一

|  |  |
| --- | --- |
| SELECT \*, SUM(**"****欄位名1", "****欄位名2"**) AS **"SUM****欄位名3, "mean("****欄位名1") as "Mean****欄位名1"**FROM ; | **PROC** **SQL**; create table kk777\_tea as SELECT \* , COUNT(D010001) AS Ckt FROM HUSALL ; **QUIT**; |

/*---*/
應用題：
我現在有一資料集，如何才能用一階段的語法以計算符合特定條件的個數？

|  |
| --- |
| **PROC** **SQL**; create table kk777\_tea as SELECT COUNT(D010001) AS Ckt  /\*  計算個數  \*/ FROM HUSALL where D010001 EQ **6**      /\*  符合特定條件  \*/ ; **QUIT**; |

推測 <改天測試>：
在這個資料集中，如果組織變數有 CORPORATE 與 LLP 二者，並且有各個縣市的區別，那麼要如何計算 組織變數的全國與縣市總數、組織變數CORPORATE的全國與縣市總數、組織變數LLP的全國與縣市總數？
我想可以用 3次 SQL 階段，與 DATA MERGE 階段 完成。
1. SQL 階段：全部組織之全國與縣市總數，用 COUNT 與 CLASS ，設成 COL1
2. SQL 階段：FIRM 之全國與縣市總數，用 COUNT ，WHERE 與 CLASS，設成 COL2
3. SQL 階段：LLP之全國與縣市總數，用 COUNT ，WHERE  與 CLASS，設成 COL3
4. DATA MERGE：MERGE COL1, COL2, COL3, SAVE AS TABLE\_ALL
符號說明：
（1）Equal to、=、EQ
（2）Greater than、>、GT→同理Greater than or equal to、>=、GE
（3）Less than、<、LT→同理Less than or equal to、<=、LE
（4）Not equal to、^=或~=或<>、NE
