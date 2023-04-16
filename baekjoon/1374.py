## 강의실 ##
from heapq import *

n = int(input())
heap = []
q = []

for _ in range(n):
    num, start, end = map(int, input().split())

    ## heap 초기화 ##
    heappush(heap,[start,end,num])
    
## 가장 시작 시간이 빠른 강의로 초기화 ##

heappush(q, heappop(heap)[1])


while(heap):
    ## q 각 원소는 강의실 ##
    ## 새로운 입력의 시작 시간 >= 가장 앞 강의 끝 시간 -> 가장 앞 강의 갱신
    ## 새로운 입력의 시작 시간 < 가장 앞 강의 끝 시간 -> 새로운 강의실 추가 (q에 원소 추가)
    start,end,num = heappop(heap)
    if start >= q[0]:
        heappop(q)
    heappush(q, end)

print(len(q))
        
    
