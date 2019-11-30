#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def reverse(self, x: int) -> int:
        y=0

        if x>0:
            while x!=0:
                y=y*10+x%10
                x=x//10
        elif x==0:
            return x
        else:
            x=-x
            while x!=0:
                y=y*10+x%10
                x=x//10
            y=-y
        if -2**31<y<2**31-1:
            return y
        else:
            return 0

