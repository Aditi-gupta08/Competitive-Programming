class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        graph = collections.defaultdict(list)
        for u,v,w in flights:
            graph[u].append((v,w))
        
    
        prices, steps = {}, {}
        
        pr_queue = [(0, 0, src)]
        heapq.heapify(pr_queue)
        
        
        while len(pr_queue)>0:
            price, step, nodeVal = heapq.heappop(pr_queue)
            print(price, step, nodeVal)
            print( pr_queue, "\n\n")
            
            if nodeVal==dst:
                return price
            
            if nodeVal not in prices:
                prices[nodeVal] = price
                
            steps[nodeVal] = step
            
            if step<=K:
                step+=1
                for n,p in graph[nodeVal]:
                    if n not in prices or step<steps[n]:
                        heapq.heappush(pr_queue, (p+price, step, n))
                    
            
        return -1