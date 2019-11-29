# Heap Sort 堆積排序法

概念:像樹狀圖一樣，每個父母下面有兩個孩子，最底層可以有缺(只有一個或沒有)。父母必須比子女大(小)，最上層的父母最大(小)。

1.max heap(最大堆積)

最上層的數字(root)必大於下面所有數

2.min heap(最小堆積)

最上層的數字(root)必小於下面所有數

# 流程圖

![流程圖](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/Heapsort%E6%B5%81%E7%A8%8B%E5%9C%96.jpg?raw=true)

# 過程

以下用max heap來說明排序過程

將list中的元素從最上方一路放下來後 由左至右 子節永遠小於父節

一但孩子比父母大 就往上移動 這樣一來最大的值就會在最上方

將最上方(最大值)拿掉 把最下方的孩子拿到第一個重新排序

不斷重複

# 參考

http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html

https://magiclen.org/heap-sort/

http://marklin-blog.logdown.com/posts/1910116

https://algorithm.yuanbin.me/zh-tw/basics_data_structure/heap.html
