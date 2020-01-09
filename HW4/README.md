# Hash Table(雜湊表)

概念:鍵值(key)通過函數(Hash Function)找到對應的位置(index)來存放(buckets)

# Hash function

概念:一個規則，將key轉換成為唯一的雜湊值輸出，方便更快速有效的找到他的index


# 舉例

1.就像是電話簿一樣，我要找王小明(key)的電話(buckets)，要如何快速從一堆人名裡找到?

從姓氏的發音[ㄨ]來找 這個規則就是Hash Function

首頁的ㄅㄆㄇ對照頁數就是index

2.buckets就像是置物櫃 拿來存放東西

index就是置物櫃的編號

Hash Function是發放置物櫃的規則

key就是大一新生名字

所以就是大一新生"丁某"(key)照著自己名字的筆劃"2畫"(Hash Function)順利地找到編號001(index)的置物櫃(buckets)

# Collision(衝突)

一般來說理想的情況是一個buckets裡面只有一個東西 

但是function可能會把兩個不同的key指向同一個index

也就是一個buckets有兩筆資料

這就會造成你用key1應該回傳item1卻回傳item2給你

## 解決方法

- 使用linkedlist把資料串起來

- 找新的空buckets存資料

# 流程圖

![流程圖](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/hashtable%E6%B5%81%E7%A8%8B%E5%9C%96.jpg?raw=true)

衝突情況

![衝突](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/collision.jpg?raw=true)

