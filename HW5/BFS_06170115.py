#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
        
    def addEdge(self,u,v): 
        self.graph[u].append(v)
        
    def BFS(self, s):
        state1=[] #s1放路徑
        state2=[] #s2最後要回傳的
        state2.append(s) #先把起點丟進s2裡面
        for i in self.graph[s]: #接著把起點的連接丟到s1裡面
            state1.append(i)
        while len(state1)>0: #當s1裡面還有東西時
            a=state1.pop(0) #把s1的第1個數字拿出來順便刪掉
            state2.append(a) #然後丟進s2裡
            for j in self.graph[a]: #然後把a的連接丟進s1裡
                if j in state2: #要檢查他在s2有沒有出現過 如果有就不用管
                    continue
                else: #沒有在s2出現過
                    if j in state1: #卻在s1出現過
                        continue #不要管
                    else: #s1s2都沒出現過就丟進s1裡
                        state1.append(j) 
        return state2 #回傳s2
    def DFS(self, s):
        stack=[] #建立空stack等下放路徑
        end=[]#等下要回傳的
        end.append(s)#先把起點丟進裡面
        for i in self.graph[s]: #接著把起點的連接丟到stack裡面
            stack.append(i)
        while len(stack)>0: #當stack裡面還有東西時
            a=stack.pop() #把stack最上層的東西拿出來 pop默認最後一個
            end.append(a) #丟到end裡
            for j in self.graph[a]: #一樣把連接丟進stack裡
                if j in end: #確認他有沒有出現過 如果有那就不用管
                    continue
                else: #沒有出現在end裡
                    if j in stack: #在stack卻出現過
                        continue #不要管
                    else: #stack跟end都沒出現過
                        stack.append(j) #丟進stack裡
        return end #回傳結果
    
#參考
#https://www.youtube.com/watch?v=QRq6p9s8NVg
#https://www.youtube.com/watch?v=oLtvUWpAnTQ&feature=youtu.be
#https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
#http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html

