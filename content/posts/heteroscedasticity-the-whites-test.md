---
categories:
- Econometrics!!!
- SAS
date: '2013-11-05T10:36:10+08:00'
draft: false
slug: heteroscedasticity-the-whites-test
tags: []
title: Heteroscedasticity & the White's test
---

如果變數的選取後，在邏輯推論上看不出來” Heteroscedasticity”(HTD)，那直接使用普通最小平方法可能可以接受。但是，文章這樣描述：「……其中，y 表示....，X 為一變數向量，用以刻畫...與依變項...息息相關。…….」息息相關等字說出” y “與” X “的選取與OLS假設衝突。因此，建議使用the White(White 1980)或 the Breusch-Pagan(Breusch and Pagan 1979) 的方法檢驗，SAS的語法在這裡：<http://support.sas.com/rnd/app/examples/ets/hetero/index.htm>。
關於 HTD 在這：<http://support.sas.com/documentation/cdl/en/etsug/66100/HTML/default/viewer.htm#etsug_panel_details33.htm>

裡頭介紹了 the White's test 與  the Breusch-Pagan test ，要解決HTD問題。
似乎可以說，White 證明nR2 服從自由度q 的卡方分配，q=(k-1)(k+2)/2  。
