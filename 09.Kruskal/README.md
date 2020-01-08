# Kruskal(克魯斯克爾)

概念:一種尋找最小生成樹的演算法。

過程:先從小到大把權重排出來，從最小權重的開始找parent把兩點連起來，重複直到所有點的parent一樣，完成連通，得到最小生成樹

# 流程圖

![k流程圖](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/Kruskal%E6%B5%81%E7%A8%8B%E5%9C%96.jpg?raw=true)

可以看到途中最小權重1是7跟6 所以6的parent是7

接著看權重2是8&2 2的parent是8

注意!第三行權重2是6跟5 可以前面6的parent是7 所以5的parent也是7

第五行權重4是2跟5 2的p 8 5的p 7 所以把p是7的全部改成8 7就不是parent了

一直重複到最後就會畫出右下角連通的圖
