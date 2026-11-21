#dfs --->  Write a Python program to represent an Undirected Weighted Graph using Adjacency List and perform Depth First Search (DFS) traversal starting from a given node.
'''n=int(input("Enter number of nodes:"))
e=int(input("Enter number of edges:"))
vertices=input("Enter vertices :").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(e):
    e,v,w=input("Enter e-v-w").split()
    graph[e].append((v,int(w)))
    graph[v].append((e,int(w)))
start=input("Enter starting node :")
visited=[]
def dfs(node):
    print(node,end=" ")
    visited.append(node)
    for v,w in graph[node]:
        if v not in visited :
            dfs(v)
dfs(start)'''



#Find all paths between two nodes in a weighted graph using Depth First Search and calculate cost of each path.
'''n=int(input("Enter number of nodes:"))
e=int(input("Enter number of edges:"))
vertices=input("Enter vertices :").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(e):
    e,v,w=input("Enter e-v-w").split()
    graph[e].append((v,int(w)))
    graph[v].append((e,int(w)))
start=input("Enter starting node :")
end=input("Enter the ending node :")
path=[]
def dfs (node,cost):
    path.append(node)
    if node == end:
        print("path:"," ".join(path))
        print("cost:",cost)
    else:
        for v,w in graph[node]:
            if v not in path:
                dfs(v,cost+w)
dfs(start,0)'''

#BFS--> Find the path between two nodes in a weighted graph using BFS traversal and calculate the cost of the path.
'''n=int(input("Enter number of nodes:"))
e=int(input("Enter number of edges:"))
vertices=input("Enter vertices :").split()
graph={}
for v in vertices:
    graph[v]=[]
for i in range(e):
    e,v,w=input("Enter e-v-w").split()
    graph[e].append((v,int(w)))
    graph[v].append((e,int(w)))
start=input("Enter starting node :")
end=input("Enter the ending node :")
queue=[(start,[start],0)]
while queue :
    node, path, cost=queue.pop(0)
    if node==end:
        print("path:"," ".join(path))
        print("cost",cost)
        break
    for v ,w in graph[node]:
        if v not in path:
            queue.append((v,path+[v],cost+w))'''



        