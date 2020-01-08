#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def twosum(nums):
    a=[]
    for i,n in enumerate(nums):
        find=target-n
        if find in nums:
            if n==find:
                a.append(i)
                if len(a)>1:
                    print(a)
            else:
                b=nums.index(n)
                c=nums.index(find)
                if b<c:
                        print([b,c])

