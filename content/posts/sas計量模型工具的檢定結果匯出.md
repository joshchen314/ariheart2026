---
categories:
- SAS
date: '2015-04-15T11:27:30+08:00'
draft: false
slug: sas計量模型工具的檢定結果匯出
tags:
- 迴歸係數
- ODS TRACE
- 參數估計值
title: SAS計量模型工具的檢定結果匯出
---

-------美麗的前言的分隔線-------
經過上面美麗的介紹後，我們都能夠體會SAS系統很好使，有許多的計量工具可以運用，最後得出美妙的檢定結果讓人滿意，尤其是SAS EG的版面配置、文字大小、字體選擇都算美觀。然而，最大的問題是，**那些檢定結果要如何運用到報告或是論文裡呢？**即使會變的很醜，我們可以有除copy and paste之外的方法。其中之一的方法如下:

|  |
| --- |
| ODS TRACE ON/ LISTING; |
| ODS OUTPUT …. ; |
| ODS TRACE OFF; |

一般我們的語法結構會是：

|  |
| --- |
| **PROC** **REG** data=…; MODEL  ….; TITLE   ….; **QUIT**; |

為了匯出檢定結果，需要在一般語法結構前後**開啟****” ODS TRACE ”**功能，並且在 **LOG****記錄檔**裡找出需要的結果，舉個以參數估計值為例子，如：

|  |
| --- |
| 已增加的輸出: ------------- **名稱****:       ParameterEstimates**標籤:        參數估計值 範本:        Stat.REG.ParameterEstimates 路徑:        Reg.MODEL1.Fit.Y.ParameterEstimates |

所以，我就需要在一般語法結構**前、後、裡面**加入一些佐料，讓料理的香氣出得來：

|  |
| --- |
| ODS TRACE ON/ LISTING; |
| PROC REG data=AGR; MODEL Y = arto / dw ; OUTPUT OUT=Z0FRESIDUAL=res PREDICTED=Yhat; **ODS OUTPUT  ParameterEstimates  =AGRO;**TITLE 'ASSUMPTION: Durbin-Watson Test of Autocorrelation'; QUIT; |
| ODS TRACE OFF; |

至於其他的如變異數分析的結果等，輸出原則也是一樣。而ODS OUTPUT 允許有許多輸出，沒有限定只有一個，所以要豪氣的全部輸出只要將對應的名稱寫對即可。
而其他的計量模型也是同樣的原則，至少我用過 QUANTREG 輸出參數估計值。我想熟悉 QUANTREG 這位朋友的應該會知道，這位好朋友會產生相當多的分位數的參數估計值，以致我根本不想手動整理。所以透過ODS TRACE功能後，就可以輸出QUANTREG分位數參數估計值，再以巨集整理數據表，最後用PROC EXPORT輸出成CSV檔，就炒出一盤好菜了。
另外，我需要做個 PROC EXPORT 與 巨集的補充。如果要以巨集的方式用PROC EXPORT語法的話，OUTFILE的地方絕對用「 " "」，而非「 ' ' 」。這是試誤法，也許看錯了。無論如何，用「 " "」可以省下麻煩。如下：

|  |  |
| --- | --- |
| 語法 | 檔案名稱 |
| outfile = "\\...\AQ1\_&A.\_&D.A.csv" | AQ1\_M\_1.csv |
| outfile = ‘\\...\AQ1\_&A.\_&D.A.csv’ | AQ1\_&A.\_&D.A.csv |

Stack Overflow也這麼說：[連結](http://stackoverflow.com/questions/13590799/how-to-import-and-export-multiple-data-using-sas-macro)。
至於從Excel到Word，可能免不了copy and paste。老實說，若是SAS也能有Knitr的話，一切就非常完美了。
