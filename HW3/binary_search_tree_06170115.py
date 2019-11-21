#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def insert(self, root, val): #root=3 insert(4)
        if root: #如果root存在
            if val>root.val: #>root往右
                if root.right: #如果右存在
                    return Solution().insert(root.right,val) #回傳繼續對比
                else: #右不存在
                    root.right=TreeNode(val) #右邊創新點
                    return root.right
            if val<=root.val: #<=root往左
                if root.left: #如果左存在
                    return Solution().insert(root.left,val) #回傳繼續對比
                else: #左不存在
                    root.left=TreeNode(val)
                    return root.left
        else: #如果root不存在
            root=TreeNode(val)
            return root
    def search(self, root, target):
        if root: #如果root存在
            if target>root.val: #往右
                if root.right: #如果右邊存在
                    return Solution().search(root.right,target) #回傳繼續找
                else: #右邊不存在 也就是找不到 回傳沒東西
                    return None
            if target<root.val: #往左
                if root.left: #如果左邊存在
                    return Solution().search(root.left,target) #回傳繼續找
                else: #左邊不存在 找不到 沒東西
                    return None
            if target==root.val: #如果要找的值=root
                return root
        else:
            return None

    def delete(self, root, target):
        if root: #如果root存在
            if target>root.val: #往右
                if root.right: #右邊存在
                    return Solution().delete(root.right,target)
            elif target<root.val: #往左
                 if root.left: #左邊存在
                    return Solution().delete(root.left,target)
            else: #等於的話
                if root.right is None and root.left is None: #如果他沒有左右子節點
                        root.val = None #把root刪掉
                return root
                if root.left: #如果只有左邊
                    if root.right is None:
                        root=root.left #替換成左邊
                        root.left.val==None
                elif root.right: #如果只有右邊
                    if root.left is None:
                        root=root.right #替換成左邊
                        root.right.val==None
                elif root.right and root.left: #如果兩邊都在
                    root.val = self.min(root.right).val#此處找最大的最小


    def min(self,root):
        if root.left is None: #如果左邊沒有值了
            return root 
        else: #左邊還有值就回傳
            return Solution().min(root.left)
    def modify(self, root, target, new_val):
        if root: #如果root存在
            if target ==root.val:
                return root
            else:
                Solution().insert(root,new_val)
                return Solution().delete(root,target)
            
#參考:https://www.itread01.com/content/1546379497.html
#http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html
#https://www.youtube.com/watch?v=YlgPi75hIBc&t=
#https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9
#老師上課講解

