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

根據left<root<right的規則來找到要新增的數的位置

如圖 新增數字[26] 先跟root1比 26>17向右走

26<32向左走 26<28放左

## 刪除

![刪除](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/%E5%88%AA%E9%99%A4.jpg?raw=true)

刪除有三種情況

- 情況1:要刪除的值沒有子節點

如圖 刪除[7] 直接把數字變成指向null就可

- 情況2:要刪除的值有一個子節點

如圖 刪除[2] 2下面還有個right(7)

將10(root2)指向7就可 因為7也是10的左節點 可以保持樹的完整性

- 情況3:要刪除的值有兩個子節點

如圖 刪除[32]

找大於(right)中的最小(如果右子節點下面還有子節點)

找小於(left)中的最大(如果下面還有子節點)

因為圖中87下面沒有其他子節點了 所以用87替代掉32

##　修改

![修改](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/%E4%BF%AE%E6%94%B9.jpg?raw=true)

修改就是想把某數改成某數

但是不能直接替換 因為這樣會有可能破壞數的結構

如圖 我不能刪掉32直接改成99

所以先新增99 接著刪掉32

所以我就直接如果root存在 新增新的數

然後回傳刪除目標

# 參考

http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html

http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html

https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9

http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html#search
