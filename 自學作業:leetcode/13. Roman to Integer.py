#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        x=0
        for i,c in enumerate(s[:-1]):
            if dict[s[i]]<dict[s[i+1]]:
                x=x-dict[s[i]]
            else:
                x=x+dict[s[i]]
        x=x+dict[s[-1]]
        return x

