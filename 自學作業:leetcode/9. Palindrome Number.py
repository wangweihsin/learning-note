#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            y=0
            z=x
            while z!=0:
                y=y*10+z%10
                z=z//10
            return x==y

