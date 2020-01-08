# Breadth-First Search (廣度優先搜尋)

概念:一層一層走下去 顧名思義以"廣度"為重點

# 流程圖

![流程圖1](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/BFS%E6%B5%81%E7%A8%8B%E5%9C%961.jpg?raw=true)

用E當起點，E連到C跟D，接著看C，C連到A跟B，接著看D，D連到F。

上課範例:

![流程圖2](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/BFS%E6%B5%81%E7%A8%8B%E5%9C%962.jpg?raw=true)

這是用C當起點，C連到EG，E連到BF，G連到E E已經出現過所以不用管，B連CF已出現過，F連A，A連D。

# Queue

把起點從頭丟進去，後續的層也照順序丟進去，保證層的順序。

# Depth-First Search (深度優先搜尋)

概念:一條走到底，直到不能走後再回頭尋找沒走訪過的點

# 流程圖

![DFS流程圖](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/DFS%E6%B5%81%E7%A8%8B%E5%9C%961.jpg?raw=true)

以A為起點 stack丟進B,C C在上層所以把C拿出來 還有C連D,E E在上拿出來 E連CD都連過了所以回頭看stack最上層現在是D D拿出來連F F連D已連過

回頭看STACK最上層是B 拿出來結束

![DFS流程圖2](https://github.com/wangweihsin/learning-note/blob/master/%E5%9C%96%E7%89%87/DFS%E6%B5%81%E7%A8%8B%E5%9C%962.jpg?raw=true)

用G當起點 stack丟進E E拿出來連B,F 最上層F拿出來連A A拿出來拿出來連D D拿出來連F已經連過回頭看最上層B拿出來 B連C 結束

# Stack

DFS用來放路徑的地方 把它想成是直立式的 把最上層的拿出來

也就是說把最後一個拿出來 讓DFS可以一條路走到底在回頭看沒走過的路徑

# BFS v.s DFS

上面提過BFS是廣度優先而DFS是深度優先

### 舉例說明:

假設我們在圖書館看到小說區 小說區裡有細分各種類別

BFS就是先了解一下小說區裡還有什麼種類 知道有奇幻、冒險類後

發現奇幻區下面還有分成魔法或是騎士類 然後看冒險類發現下面還分成東西方

DFS的話是直接走進小說區裡第一個冒險類逛然後接著逛冒險下的魔法一條路到底逛完後 再出來往沒逛過的走進去逛到底

### 路徑

BFS用的state是先進先出

DFS用的stack是先進後出

### 複雜度

BFS 空間複雜度 O(|V|+|E|) 時間複雜度 O(|V|+|E|)

DFS 空間複雜度 O(bm) 時間複雜度 O(b^m)

BFS適合大範圍尋找 比較需要記憶體

DFS適合目標明確的 比較節省記憶體
