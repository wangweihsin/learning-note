#!/usr/bin/env python
# coding: utf-8

# In[1]:


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
        father=None
        node=root
        while node and node.val!=target:
            father=node
            if target>node.val:#往右
                node=node.right
            elif target<node.val:#往左
                node=node.left
            #如果相等就會跳出去 此時father=5 node=3
            
        if node is None: #要記得設node沒有值跳出來的狀況
            return root
        if node.right is None and node.left is None:#沒有子節點
            node=None #直接刪除
            if target>father.val:
                father.right=node
            else:
                father.left=node
            return root

        if node.left: #只有左節點
            if node.right is None:
                if target< father.val:
                    father.left=node.left
                    return self.delete(root,target)
        if node.right: #只有右節點
            if node.left is None:
                if target> father.val:
                    father.right=node.right
                    return self.delete(root,target)
        if node.right and node.left: #如果兩邊存在
            minnode= self.findmin(node.right)
            node=minnode
        return root
    def findmin(self,root):
        if root.left:
            return self.findmin(node.right)
        else:
            return root
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

