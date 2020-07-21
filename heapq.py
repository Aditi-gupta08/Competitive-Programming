import heapq, queue
h = []
heapq.heappush(h, (5, 'write code'))
heapq.heappush(h, (7, 'release product'))
heapq.heappush(h, (1, 'write spec'))
heapq.heappush(h, (3, 'create tests'))
print(heapq.heappop(h))


h2 = [(5, 'write code'), (7, 'release product'), (1, 'write spec'), (3, 'create tests')]
heapq.heapify(h2)
print(heapq.heappop(h2))

q = queue.PriorityQueue()
q.put((5, 'write code'))
q.put((7, 'release product'))
q.put((1, 'write spec'))

print(q.get())