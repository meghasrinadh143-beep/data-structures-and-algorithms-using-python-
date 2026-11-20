#Graphs if the in the exam if they tell consider vertices it is graphd and if they teel consider nodes it is nodes in python 
#un weighted -- All edges are equal, no number on line.  Example: A - B, distance is just 1 step. BFS is used here.
#Weighted    -- Every edge has a number / cost / distance.Example: A -5- B, A -2- C. Dijkstra is used here.
#directed    -- One-way road. A -> B only, B cannot go to A.
#undirected  -- Two-way road. A - B, both can go to each other.
#BFS         -- (Breadth First Search) Level by level visits. Uses Queue.Best for Shortest Path in Unweighted graph.
#DFS         -- (Depth First Search) One road deep till end, then back. Uses Stack / Recursion.Best for Maze, checking all paths, cycle detection.
#shortest path 




#create a graph and connect the nodes unwaighted and undirected graph 
'''n=int(input("Enter number of vertices:"))
e=int(input("Enter number of edges:"))
vertices=input("Enter vertices").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(e):
    e,v=input("Enter edge:").split()
    graph[e].append(v)
    graph[v].append(e)
for v in graph:
    print(v,"->",graph[v])'''
    

#creating a graph and connection the nodes with weight is weighted and directed graph 
n=int(input("Enter number of vertices:"))
v=int(input("Enter number of nodes:"))
vertices=input("Enter vertices:").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(n):
    n,v,w=input("Enter edges:").split()
    w=int(w)
    graph[n].append((v,w))
    graph[v].append((n,w))
for v in graph:
    print(v,"->",graph[v])