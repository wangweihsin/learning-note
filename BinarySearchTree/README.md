# binary search tree (二元搜尋樹)

概念:將比根植小的數放左邊，比根植大的樹放右邊，left child<root<right child，子節點不一定有兩個。

# 流程圖

![流程圖](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/binary%20tree%E6%B5%81%E7%A8%8B%E5%9C%96.jpg?raw=true)

# 功能

## 搜尋

![搜尋](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/%E6%90%9C%E5%B0%8B.jpg)

根據binary search tree的規則left<root<right進行搜尋

- 搜尋成功

將搜尋的值與root對比 像圖中找[2] 2<17(root1)所以往left走

2<10(root2)再繼續往left走 就找到2了

- 搜尋失敗

另一種情況是沒有搜尋到 像圖中找[54]

54>17(root1)向right走 54>32(root3)向right走

但是32沒有right 於是回傳null

## 新增

![新增](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/%E6%96%B0%E5%A2%9E.jpg)

## 刪除

![刪除](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/%E5%88%AA%E9%99%A4.jpg?raw=true)

##　修改

![修改](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/%E4%BF%AE%E6%94%B9.jpg?raw=true)

# 參考

http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html

http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html

https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9

http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html#search
