---
categories:
- SAS
- SAS 101
date: '2014-04-25T03:16:57+08:00'
draft: false
slug: sas-101-day-4-資料輸出與ods
tags: []
title: SAS 101 Day 4 資料輸出與ODS
---

我原先單細胞腦子這樣想：資料輸出很簡單，不就COPY AND PASTE就好了。但這是SAS，可是花了一堆$$，結果還是用 C & P 就不潮了，所以我們就來看 這個新潮的系統 Output Delivery System。不過，先來看顯而易見的部分，就是 ODS 可以將輸出的資料轉成資料集，繼續在 DATA階段料理。以下是相關的文件：
<http://www.sasresource.com/faq21.html>
<http://www.loyhome.com/learning-sas-in-7-days-4/>
<http://www2.cmu.edu.tw/~biostat/online/teaching_corner_061_2.pdf>

先給個 boats.csv

|  |
| --- |
| Silent Lady,Maalea,sail,sch,75,153 America II,Maalea,sail,yac,32.95,125 Aloha Anai,Lahaina,sail,cat,62,117 Ocean Spirit,Maalea,power,cat,22,162 Anuenue,Maalea,sail,sch,47.5,111 Hana Lei,Maalea,power,cat,28.99,115 Leilani,Maalea,power,yac,19.99,119 Kalakaua,Maalea,power,cat,29.5,134 Reef Runner,Lahaina,power,yac,29.95,126 Blue Dolphin,Maalea,sail,cat,42.95,124 |

|  |
| --- |
| **DATA** boats; INFILE'c:\MyRawData\boats.csv'   DLM =','   DSD     MISSOVER; INPUT BoatsName :$15. Location :$10. Power: $7. Type: $5. Cost: 8. Len: 8. ; RUN; |

|  |
| --- |
| /\*Statistics in COLUMN statement with two group  variables; \*/ ODS output report=work.t1; **PROC** **REPORT** DATA = boats  NOWINDOWS HEADLINE; COLUMN Location Power N (Cost LEN), MEAN; DEFINE Location / GROUP; DEFINE Power / GROUP; TITLE 'Statistics with Two Group Variables'; **RUN**;ODS OUTPUT close; ODS  output report=work.t2;\*Statistics in COLUMN statement with group and across variables;**PROC** **REPORT** DATA = boats NOWINDOWS HEADLINE; COLUMN Location N Power,  (Cost LEN), MEAN; DEFINE Location / GROUP; DEFINE Power / ACROSS; TITLE 'Statistics with a Group and Across Variable'; **RUN**; ODS OUTPUT close; |

**“ODS****output** **report=work.t2;”** **與** **“****ODS****OUTPUT****close****;”** 可以將result viewer的資料表匯到資料集（如”WORk”）中
 
**ODS TRACE ON** **與****ODS TRACE OFF** 可以追蹤資料的足跡，裡邊會有Path的資料位置
 
**ODS SELECT ---** 可以只生成Path的資料位置的部分資料
 
**以下是  SAS 產生的報表，SAS 上比較美。**//

|  |
| --- |
| Statistics with Two Group Variables |

|  | | | Cost | Len |
| --- | --- | --- | --- | --- |
| Location | Power | N | MEAN | MEAN |
| Lahaina | power | 1 | 29.95 | 126 |
|  | sail | 1 | 62 | 117 |
| Maalea | power | 4 | 25.12 | 132.5 |
|  | sail | 4 | 49.6 | 128.25 |

---

|  |
| --- |
| Statistics with a Group and Across Variable |

|  | | Power | | | |
| --- | --- | --- | --- | --- | --- |
|  | | power | | sail | |
|  | | Cost | Len | Cost | Len |
| Location | N | MEAN | MEAN | MEAN | MEAN |
| Lahaina | 2 | 29.95 | 126 | 62 | 117 |
| Maalea | 8 | 25.12 | 132.5 | 49.6 | 128.25 |

總結，給了清楚的 RAW DATA 後，真的比較好複習，也體會到 SAS ODS 很好很強大。
最後需要大推薦：[落園 七天搞定SAS 系列](http://www.loyhome.com/learn-sas-in-7-days-index/)。其中，第三、四部分的資料輸出部分，博主體會很深，整理非常清楚。
