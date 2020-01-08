#!/usr/bin/env python
# coding: utf-8

# In[10]:


def QuickSort(alist):
    left=[] 
    center=[]
    right=[]
    if len(alist)<=1: #如果alist裡只有一個或沒有元素就不用排序
        return alist
    else:
        import random
        key=random.sample(alist,1)
        key=key[0]
        for i in alist:
            if i>key:  
                right.append(i)
            elif i<key: 
                left.append(i)
            else:
                center.append(i)
    left=QuickSort(left)
    right=QuickSort(right)
    return left+center+right

