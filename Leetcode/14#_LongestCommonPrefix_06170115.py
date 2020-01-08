#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def longestCommonPrefix(self, strs:list) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        end=""
        for k in range(len(strs[0])):
            x = strs[0][0:k+1] #第一個數
            for i in range(1,len(strs)): #跟第2第三個作對比
                y=strs[i][0:k+1]
                if x!=y:
                    break
            else:
                end= x
                continue
            break
        return end
Solution().longestCommonPrefix(["flower","flow","flight"])

