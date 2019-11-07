#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution(object):
    def heap_sort(self,nums): #前面隨便塞個數
        self.nums=nums
        nums=[0]+nums
        return heap(nums)
    def heap(alist):
        for i in range(len(alist)//2,0,-1):
            root=i
            left=2*i
            right=2*i+1
            if left<len(alist): #左節點
                father=alist[root]#父節點
                leftson=alist[left]
                if leftson<father:     #如果左節點比父節點小
                    a=alist[root]
                    alist[root]=alist[left]
                    alist[left]=a #左節點跟父節點互換
            if right<len(alist): #右節點
                father=alist[root]#父節點
                rightson=alist[right]
                if rightson<father: #如果右節點比父節點小
                    a=alist[root] #父跟右換
                    alist[root]=alist[right]
                    alist[right]=a
        return newlist(alist)

    def newlist(alist):
        x=[]
        if len(alist)>1:
            x.append(alist[1]) #把最小的丟到新list裡

            a=alist[1] #跟最後一個互換
            alist[1]=alist[len(alist)-1]
            alist[len(alist)-1]=a

            alist.pop(len(alist)-1) #去掉最後一位
            return x+heap(alist)
        else:
            return x

