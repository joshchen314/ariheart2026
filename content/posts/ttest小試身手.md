---
categories:
- 這是抄的！
- SAS
date: '2013-10-29T03:27:30+08:00'
draft: false
slug: ttest小試身手
tags: []
title: ttest小試身手
---

<http://www.pt.ntu.edu.tw/hmchai/SAS/Index.htm>
> ```
> proc sort data=ok.reach;
>      by gender;
> proc ttest data=ok.reach;
>      class gender;
>      var age bw bh bmi foot;
> run;
> ```

由於 Student-t 檢定需分組，故應先排序，否則無法執行統計運算。

|  |
| --- |
| **變項 age**： 先檢測兩組間的變異數是否相同，即參考「equality of variances」的資料，發現 F6 = 6.83, *p* < 0.05，故推翻虛無假設，即二組間的變異數存在統計學差異，所以本研究樣本不符合獨立 *t*檢定的「二組變異數相同」的前提假設。因此應選擇 Satterthwaite Method 計算 *t* 值。*t*值結果 顯示在「T-Tests」的資料，發現變項 age 之 t7.72 = 0, *p* > 0.05，故須接受虛無假設 H0：m1 = m2，表示受試者在不同性別間的平均年齡不存在統計學上顯著的差異，亦即男性的平均年齡與女性的並無不同。**變項 foot**： 檢測兩組間的變異數是否相同，發現 F6 = 1.52, *p* > 0.05，故二組間的變異數並無不同，所以本研究樣本符合獨立*t* 檢定的「二組變異數相同」的前提假設。因此應選擇 Pooled Method 計算*t* 值。*t*值結果發現變項 foot 之 t12 = 3.57, *p* < 0.005，推翻虛無假設 H0：m1 = m2，表示受試者在不同性別間的平均足長存在統計學上顯著的差異，亦即男性的平均足長與女性的有顯著的不同。 **Statistics**： 列出所有變項身高的平均值、標準差、95% CI 等統計值。 |
