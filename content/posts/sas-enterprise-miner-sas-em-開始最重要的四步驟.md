---
categories:
- 這是抄的！
- SAS
date: '2013-10-29T02:12:12+08:00'
draft: false
slug: sas-enterprise-miner-sas-em-開始最重要的四步驟
tags: []
title: SAS Enterprise Miner (SAS EM) 開始最重要的四步驟
---

SAS Enterprise Miner (SAS EM) 開始最重要的四步驟

by TKU IM EMBA Students (2012)

Version 2012.04.13

SAS\_EM開始最重要四步驟：

Step 1. Create Project (建project)

Step 2. Define Library (建Library)

Step 3. New Data Source (Input Data Set)(指定db source)

Step 4. Create Diagram (Diagram流程圖)\

\
1. 建project
\

\

\
1. 建Library（db）以table放在資料夾的(.sas7bdat)
\

\
請指定資料夾，非資料夾內的檔案（D:\SASEMData）\

\
1. 指定db source
\

\
欄位名稱及角色

1.一定要有Target當Y變數

2.input為X變數

Interval：在decision tree會產生平均值，如：購買幾次

若改為Binary為0/1 or yes/no（如：1=好0=壞客戶、yes=會no=不會買）

選Raw data

觀察資料：改最大值(Max)，講義後面章節P.72有資料庫欄位說明（預設為2000筆，改完為3000筆）

Plot

Bin：區塊

Pie

區分好壞客戶(0.1)

1:壞客戶:500

0:好客戶:2500

選擇部份區塊，可自動在Pie上看出分佈狀況\

\
1. Diagram流程圖（Decision Tree）
\

\
增加節點：（拖拉）

要將3000筆分成訓練資料70%跟驗證資料30%

改測試筆數比例：

結果：

加入決策樹\

\
1. 自建決策樹
\

\
Train:Interactive

以下為：target的level屬性設為：Interval：在decision tree會產生平均值，

就會出現以下畫面

-Log(p)愈大，變數愈重要（影響力比較大）

粗線代表：人數最大宗(一般性rule)，若經費有限就是會先選擇

以下為：target的level屬性設為：Binary為0/1 or yes/no（如：0=好1=壞客戶、yes=會no=不會買）

粗線代表：人數最大宗(一般性rule)，若經費有限就是會先選擇

（粗細代表人數的佔比）

修技：

正常：

不正常或過於極端：以Validation為主，二個若發散就為不好，則要從發散後開始修技（保留３，從４開始刪，Validation要往train方向）

可以從發散的開始修

切三個：

References:

<http://mail.tku.edu.tw/myday/teaching.htm#1002BI>
