## 절댓값 힙 ##
from heapq import *

n = int(input())
ary = []
res = []

for _ in range(n):
    x = int(input())
    ## 배열 내에서 절댓값이 가장 작은 원소를 그때그때 저장해놈
    if x != 0:
        heappush(ary,(abs(x),x))
    else:
        if len(ary) !=0 :
            absolute, origin = heappop(ary)
            res.append(origin)
        else:
            res.append(0)

    
  
for i in res:
    print(i)  
# print('\n'.join(res))
        