#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from Crypto.Hash import MD5
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None #linklist的點

class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity #這邊要可更改 所以不要設成=5
        self.data = [None] * capacity #要存放的抽屜
        
    def md5(self,key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x= h.hexdigest()
        x=int(x,16) #轉成10進位
        return x #回傳加密後的 等下要用這個狀態存進去
    
    def add(self,key):
        key=self.md5(key)
        index=key%self.capacity #索引號就是剛剛md5轉完的餘數
        if self.data[index]: #如果裡面有東西
            y=self.data[index]
            while y.next: #當他下一個存在
                y=y.next #頭變成下一個
            y.next=ListNode(key)     #如果下一個不存在就變成新的點
        else: #裡面沒東西就建立點
            self.data[index]=ListNode(key) 
        return self.data[index].val
    
    def contains(self, key):
        key=self.md5(key)
        index=key%self.capacity #索引號就是剛剛md5轉完的餘數
        if self.data[index]:#如果裡面有東西
            if self.data[index].val==key:#如果裡面就是key
                return True
            else:
                y=self.data[index]
                while y.next: #當他下一個存在
                    if y.next.val==key: #如果下一個就是key
                        return True
                    else:
                        y=y.next #不是的話頭就變下一個繼續找
                return False #如果找到他下一個都不存在還找不到就會傳false
        else: #裡面沒東西
            return False
 
    def remove(self, key):
        x=self.md5(key)
        index=x%self.capacity #索引號就是剛剛md5轉完的餘數
        if self.contains(key)==True: #如果裡面有要刪的數字
            if self.data[index].val==x: #如果第一個就是要刪掉的數
                if self.data[index].next: #如果他下一個存在
                    self.data[index]=self.data[index].next #頭就變下一個不然找不到下一個東西
                else: #如果他下一個不存在就直接刪掉
                    self.data[index]=None #刪掉他
            else: #如果不是第一個就往後找
                y=self.data[index]
                while y.next: #當他下一個存在
                    if y.next.val==x: #如果下一個就是key
                        if y.next.next: #如果key後面有東西
                            y.next=y.next.next #就變成下下個
                        else: #key後面沒東西
                            y.next=None #刪掉
                    else:
                        y=y.next #不是的話頭就變下一個繼續找  
            return self.remove(key) #避免重複值
        else: #沒要刪的
            return False
        
#參考:https://www.youtube.com/watch?v=aZVNWYSR_sY&feature=youtu.be
#https://github.com/graphoarty/python-dsa/blob/master/DataStructures/HashTable/HashTable.py
#https://github.com/joeyajames/Python/blob/master/HashMap.py
#https://medium.com/100-days-of-python/day-09-hash-table-chaining-ef74baa6732
#https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/

