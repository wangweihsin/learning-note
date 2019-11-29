# Merge Sort 合併排序法

概念:將大的問題分解成很多個小問題，從小的問題開始解決起。把小事解決完以後合併回大問題，大問題自然就解決了。

# 流程圖

![流程圖](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/MergeSort%E6%B5%81%E7%A8%8B%E5%9C%96.jpg?raw=true)

# 分解與合併

Merge Sorty主要步驟就是1.拆分2.合併

## 分解

將list從中間切一半分成兩個小list

大--->中--->小

一直對半分，直到list中只剩一個元素沒辦法再分成兩個list為止。

## 合併

左右兩個list比較排序 從各自的第一個數字開始排序 比較大的就先放到list裡

兩兩比較直到某個list裡的數字先沒了 剩下那個list的數字就可以直接放下去

ex:[10,17] [2,32,65] 2跟10比2先放下去 接個10跟32比10放下去 17跟32比17放下去

[2,10,17, , ]<--變成這樣

此時左邊的list已經空了 右邊剩[32,65]就可以直接放下去

因為前面已經排序過了!

# 參考

http://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html

http://notepad.yehyeh.net/Content/Algorithm/Sort/Merge/Merge.php

https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e
