---
categories:
- SAS
- SAS 101
date: '2014-04-25T03:22:30+08:00'
draft: false
slug: sas-101-day-5-資料集合併與分割
tags: []
title: SAS 101 Day 5 資料集合併與分割
---

工作上比較常用到垂直合併與水平合併。比較需要注意的是水平合併，需要先排順序，按照某一行變量作為相同元素作合併。

1. 生成新變量（行） CPV，本例中加上四捨五入至小數點第二位。

|  |
| --- |
| **DATA** boats; INFILE 'c:\MyRawData\Boats.csv' DLM=',' DSD MISSOVER; INPUT Name :$13.  Port :$7.  Locomotion :$5.  Type :$3.  Price Length; RUN; **DATA** BT1; SET BOATS; CPV=ROUND(Price / Length \* **100**, **0.01**); RUN; |

2. 垂直合併多個資料集
   先產生 Boats2.csv 後再進行操作：

|  |
| --- |
| Kaohsiung,Maalea,sail,cat,34.5,113 Reading,Lahaina,power,yac,26.34,131 Madrid,Maalea,sail,yac,42.95,154 |
| **DATA** boats2; INFILE 'c:\MyRawData\Boats2.csv' DLM =',' DSD MISSOVER; INPUT Name:$13.  Port:$7.  Locomotion:$5.  Type:$3.  Price Length; RUN; |
| **DATA** BT2; **SET BT1 BOATS2;**CPV=ROUND(Price / Length \* **100**, **0.01**); RUN; |

第一要先確定行變量完全相同且對準，可以允許不完全相同，但是一定要對準。也就是說，**多個資料集的行變量的名稱要完全相同**，不然，SAS視為新變量。概念上，就是SAS先讀第一個資料集，再讀第二個資料集，以下類推，而結果剛好合併了。

3. 水平合併多個資料集

也就是說，每一筆列資料增加多筆行變量。當然，先產生 Boats3.csv 再進行操作：

|  |
| --- |
| Silent Lady,5.1 America II,2.5 Aloha Anai,1.9 Ocean Spirit,6.1 Anuenue,1.1 Hana Lei,1.5 Leilani,1.9 Kalakaua,3.1 Reef Runner,2.9 Blue Dolphin,2.1 Kaohsiung,1.1 Reading,3.1 Madrid,5.3 |
| **DATA** boats3; INFILE 'c:\MyRawData\Boats3.csv' DLM =',' DSD MISSOVER; INPUT Name :$13. **rate**; RUN; |
| **proc****sort**data=bt2;  by name; **proc****sort**data=boats3;  by name; **DATA** BT3; **MERGE** BT2(IN=A)  boats3(IN=B); BY Name; IF A; run; |

 
第一步驟要先確定多個資料集按照某個行變量（這裡是：”Name”）排順序，所以用 ” **proc****sort** ”。第二步驟才是合併，用 “ MERGE ” 。然後，每一筆資料就會新增行變量，這裡是 rate 。
這裡需要說明的是 "IF" 的用法：
IF A          保留完整A集合
IF A & B  匯出A集合與B集合的交集
IF A | B   匯出A集合與B集合的聯集，也就是等同不要帶出"IF"

4. 資料集分裂

白話講，就是一分為多。

|  |
| --- |
| **DATA** BT4cat BT4yac BT4sch; set BT3; IF TYPE = 'cat' THEN OUTPUT BT4cat; ELSE IF TYPE = 'yac' THEN OUTPUT BT4yac; ELSE IF TYPE = 'sch' THEN OUTPUT BT4sch; run; |

Set 讀取來源
**DATA** 烹調出多個資料集（可說是子集）
If then else if 用條件決定如何分裂資料集。如果是”… THEN  OUTPUT …” ，那3個資料集都有。

5. 資料集轉置

|  |
| --- |
| **proc****transpose**data = bt3 out=bt5; var Name port Locomotion type price length; **run**; |

 
Var 要轉的行變量
Id  轉置後，作為行變量的 變數名稱
Class  分組轉置
“transpose”與“class”非常好用。因為在proc summary階段出來的很有可能是分組資料。為了資料應用轉成矩陣格式，我曾經手動將一段一段資料用excel轉置，費了千辛萬苦，還怕出錯。現在，我可以用“transpose”+“class”，不到5行就完成了。
