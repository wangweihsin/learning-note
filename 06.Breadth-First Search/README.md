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
