# Transitive Closure of a Graph using DFS (Geeks for geeks - dfs ques2)

import collections

def dfs(graph, n, src):
    q = [src]
    visited = [0]*n
    visited[src] = 1
    
    while(len(q)>0):
        
        top = q.pop(0)
        
        for neigh in graph[top]:
            if visited[neigh] == 0:
                visited[neigh] = 1
                q.append(neigh)
        
    return visited
    

    
n = 4
lst = [[0,1], [0,2], [1,2], [2, 0], [2,3], [3,3]]
graph = collections.defaultdict(list)

for u,v in lst:
    graph[u].append(v)
    

res = []

# Calling dfs for each node to check the nodes which can be visited from it
for i in range(n):
    res.append( dfs(graph, n, i) )
print(res)