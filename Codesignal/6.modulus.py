#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#題目：辨別n是否為整數
def modulus(n):
    if type(n)==int: #如果n的類型為整數則輸出n/2的餘數=1
        return n % 2
    else:
        return -1

