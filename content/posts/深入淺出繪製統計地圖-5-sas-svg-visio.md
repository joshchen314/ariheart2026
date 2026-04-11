---
categories:
- 統計地圖
date: '2017-07-18T23:35:04+08:00'
draft: false
slug: 深入淺出繪製統計地圖-5-sas、svg、visio
tags: []
title: 深入淺出繪製統計地圖 5 – SAS、SVG、Visio
---

SVG是可縮放向量圖形（Scalable Vector Graphics）的簡稱，也就是說，最大特色就是「向量」，不僅不失真，更能夠無限縮放的一種圖形格式，另一種常見的可攜式網路點陣圖形檔（Portable Network Graphics，PNG）在多次放大後會顯示出點陣圖或馬賽克。因此，許多的資料視覺化工具都會支援SVG格式，尤其是D3.js。

不過，這一篇是要簡單介紹在SAS系統中，如何將Proc GMAP繪製的地圖匯出成希望的檔案格式。目前，SAS非常強大地支援SVG、PNG、TIFF、JPG等檔案格式。但是，這裏要特別推薦的當然是SVG檔，不僅圖檔非常完整，而且匯出成SVG檔案後，還能夠以 InkScape 或是 MS Visio 進行編輯（尤其是標籤的部分（我都要感動地掉眼淚了））！！！

1. SAS以ODS實現

ODS功能真的很強大，也支援SVG檔的匯出，語法如下：

FILENAME GRAFOUT "D:\SAS\DesDSN\SVGTEST.SVG";\
GOPTIONS DEVICE=SVG GSFNAME=OUT GSFMODE=replace;\
ODS LISTING;\
PROC GMAP GOUT=MAPCHART\
DATA=WORK.MAPCHARTRESPONSEPREP MAP=WORK.MAPCHARTMAPPREP ALL ;

這樣，SVG檔就會存在指定資料夾裡。

2.編輯SVG檔

PROC GMAP功能可以為統計地圖加上縣市標籤，但是，有時候會對縣市標籤的字體、大小、顏色、位置等細節進行微調。一般來說，PNG、TIFF、JPG等檔案格式會將縣市標籤嵌入統計地圖，就不能繼續編輯了。這時候，SVG檔的強項就顯現出來了，因為ODS匯出地圖的SVG檔，不會將縣市標籤嵌入統計地圖，也就是說，即使從SAS匯出圖檔之後還能繼續編輯統計地圖。

3.編輯SVG檔 Part II : InkScape （2017/9/14 update）

恭喜老爺，賀喜夫人！！！ 我終於可以用開放軟體 InkScape 編輯 SVG檔了。事情是這樣的，之前其實已經知道 InkScape 可以編輯 SVG檔，但是從 SAS 匯出的向量檔在 InkScape 開啟，總是會遇到問題，就是左下方會有一陀黑黑的物體，不知道什麼原因。就在今天突然想到，開放軟體有時候中文支援不給力，很正常的。所以，嘗試點擊那陀黑色區塊，改一種字體後，一切都非常美好了。因此，就是字體問題（OS：我都特地選「標楷體」還這樣）。

好的，變通方法是這樣，在 SAS PROC GMAP 的方法裡的圖例格式，所選用的字體應該使用英文字體，如「Calibri」等。也就是說，即使是中文字，如「普查家數」，也選用「Calibri」。雖然這將在SAS顯示出現錯誤，但是，InkScape會是完美顯示。

代碼範例：

LEGEND1\
DOWN=&LVD  FRAME POSITION=(BOTTOM LEFT OUTSIDE)\
LABEL=(FONT='Calibri' HEIGHT=9pt JUSTIFY=LEFT position=TOP &UE)\
VALUE=(HEIGHT=12pt FONT='Calibri');
