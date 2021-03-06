#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from collections import defaultdict 
class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
    def Dijkstra(self, s):
        row=len(self.graph[0])#看第一行有多少數就是結果要返回的0~?
        distance = [float("inf")] * row #所有的路徑先都等於inf
        distance[s]=0 #起點等於0
        
        queue=[]#放數字的list 還沒走過的點
        for j in range(row):
            queue.append(j)
        
        #找起點後連接的點 0-1
        x=[] #先設個空list等下放我要找的除了0以外的數字
        for i in self.graph[s]:#看起點那行
            if i>0: #大於0的數字
                x.append(i) #丟進x裡
        y=self.graph[s].index(min(x)) #找除了0以外最小的數字所在的位置  
        distance[y]=min(x)

        while queue: #當還有沒走過的點 queue(1,2,3,4,5,6,7,8)
            u=self.mindistance(distance,queue) #看他下一個要往哪走 0-1-? u=2
            queue.remove(u)
            for v in range(row):
                if v in queue: #如果v還沒走過
                    if self.graph[u][v]>0: #他有連到那個點
                        if distance[u]+self.graph[u][v]<distance[v]:
                            distance[v]=distance[u]+self.graph[u][v]
        
        return self.endreturn(distance)       
    def mindistance(self,distance,queue): #找下個最近的點
        mindist = float("inf")
        for k in range(len(self.graph[0])):
            if k in queue:
                if distance[k] < mindist:
                    mindist = distance[k]
                    minindex = k
        return minindex
    def endreturn(self,distance):
        end={} #最後要回傳的字典
        for d in range(len(self.graph[0])): #看他一行有幾個數字
            end[str(d)]=distance[d] #先建立在字典裡 後面的值先寫None之後補
        return end
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
    def Kruskal(self):
        
        p=[-1]*self.V #parent設-1
        self.graph=sorted(self.graph,key=lambda item:item[2]) #照權重排列
        end={}
        for i in range(len(self.graph)):
            a=self.graph[i][0]#第一小的權重
            b=self.graph[i][1]
            if p[a] and p[b] == -1:
                p[a]=a
                p[b]=a
                end[str(a)+"-"+str(b)]=self.graph[i][2]
                
            if p[a]==-1:
                if p[b]!=-1:
                    p[a]=a
                    for j in p:
                        if p[j]==p[b]:
                            p[j]=a
                            p[b]=a
                    end[str(a)+"-"+str(b)]=self.graph[i][2]
            if p[a]!=-1:
                if p[b]==-1:
                    p[b]=p[a]
                    end[str(a)+"-"+str(b)]=self.graph[i][2]
        return end
#參考:https://www.geeksforgeeks.org/printing-paths-dijkstras-shortest-path-algorithm/
#https://www.youtube.com/watch?v=9wV1VxlfBlI
#http://design2u.me/blog/33/python-list-%E4%B8%B2%E5%88%97-%E8%88%87-dictionary-%E5%AD%97%E5%85%B8-%E5%9F%BA%E6%9C%AC%E6%8C%87%E4%BB%A4
#https://www.runoob.com/python/python-func-zip.html
#https://www.runoob.com/python/python-dictionary.html

