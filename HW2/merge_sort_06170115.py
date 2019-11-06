#!/usr/bin/env python
# coding: utf-8

# In[68]:


class Solution(object):
    def merge_sort(self,nums):
        self.nums=nums
        if len(nums)<=1:
            return nums
        else:
            a=len(nums)
            b=a//2
            left=nums[0:b]
            right=nums[b:a]
        left=Solution().merge_sort(left)
        right=Solution().merge_sort(right)
        return Solution().Conquer(left,right)
    def Conquer(self,left,right):
        self.left=left
        self.right=right
        x=[]
        if len(left)==0:
            return right
        if len(right)==0:
            return left
        if left[0]>right[0]:
            x.append(right[0])
            right.pop(0)
            return x+Solution().Conquer(left,right)
        else:
            x.append(left[0])
            left.pop(0)
        return x+Solution().Conquer(left,right)

