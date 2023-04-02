## 소수의 곱 ##
from heapq import *

k,n = map(int, input().split())
num = list(map(int, input().split()))

heap = []
max_val = max(num)
visited = set()

for data in num:
    heappush(heap, data)
    
for _ in range(n-1):
    element = heappop(heap)
    for data in num:
        now = element * data
        if len(heap)>=n and max_val < now:
            continue
        if now not in visited:
            heappush(heap, now)
            max_val = max(max_val, now)
            visited.add(now)

print(heappop(heap))
