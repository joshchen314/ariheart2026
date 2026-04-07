---
categories: []
date: '2017-04-05T22:45:18+08:00'
draft: false
slug: iis-php-mariadb-wordpress
tags: []
title: IIS + php + MariaDB + WordPress
---

這個架站組合是比較偏向現代化的組合（以我淺薄知識的認為），並且採用Windows本機來提供服務（相對於Google上找到的都是在雲端供應商居多）。至於為什麼使用本機端架站呢？答案很簡單，就是測試。

1. IIS與php
   [這個網頁](http://mirlab.org/users/PONY.CHEN/note/phpAndMySQL_on_Win7_x64_IIS7.asp?title=%A6bWindows+7+x64%A5%AD%A5x%AA%BAIIS%AC%5B%B3%5DPHP%BBPMySQL)提供了這兩個功能的設定。

2.MariaDB
安裝好之後，自帶 HeidiSQL軟體（取代phpMyadmin，我被打敗了），隨便找一個[簡單教學](https://read01.com/DGaG0B.html)。按照該教學裡的「創建數據表」節，建立一個數據集（例：「WP\_r2d2」），供WordPress使用。
3.WordPressd
按照WordPress的[5分鐘教學](https://codex.wordpress.org/zh-tw:%E5%AE%89%E8%A3%9DWordPress#5.E5.88.86.E9.90.98.E5.9C.A8Windows.E8.BC.95.E9.AC.86.E5.AE.89.E8.A3.9DWordPress)，要注意的是資料庫的資訊除了帳號與密碼外，還必須給一個資料庫的數據集（如上段例：「WP\_r2d2」）。
這是目前進度，瀏覽器在localhost後會有網頁，之後還有ip與網站位址之類的課題，之後更新。
更為現代化的組合應該是直接採用Node.js體系，使用Ghost部落格系統，但是，這一個生態系還不知道如何進入，只好先用較為成熟的WordPress系統。
