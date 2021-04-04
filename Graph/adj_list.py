# Dijisktra implementation using adjacency list & priority queue 

from collections import defaultdict
import heapq

def print_res(dist):
    print("\n\nFinal Result :: ")
    print("Vertex   Distance from source")
    for i in range(len(dist)):
        print(i, "\t\t", dist[i])
    
    
def print_step(u, dist):
    print(u, end="\t\t")
    for i in range(len(dist)):
        print(dist[i], end="  ")
    print("\n")



def dijikstra(graph, src):
    dist = [float('inf')]*(len(graph))
    
    dist[src] = 0
    pr_queue = [(0, src)]
    heapq.heapify(pr_queue)
    visited = [False]*(len(graph))
    
    
    for i in range(len(graph)):
        elem, u = heapq.heappop(pr_queue)
        
        for v, w in graph[u]:
            
            if visited[v]==False and w>0:
                if (dist[u]+ w) < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pr_queue, (dist[v], v))
   
        visited[u] = True

        print_step(u, dist)
    print_res(dist)
    
    
    

v = int(input())
n = int(input())
graph = defaultdict(list)

for i in range(n):
    u, v, w = map( int, input().rstrip().split(" "))
    graph[u].append((v, w))
    graph[v].append((u, w))
    
dijikstra(graph, 0)