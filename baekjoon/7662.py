## 이중 우선순위 큐 ##
from heapq import *
def pop(heap):
    while len(heap) > 0:
        data, id = heappop(heap)
        if not deleted[id]:
            deleted[id] = True
            return data
    return None

for _ in range(int(input())):
    k = int(input())
    min_heap = []
    max_heap = []
    current = 0
    deleted = [False] * (k+1)
    
    for i in range(k):
        cmd = input().split()
        oper, data = cmd[0], int(cmd[1])
        if oper == 'D':
            if data == 1:
                pop(max_heap)
            elif data == -1:
                pop(min_heap)
        elif oper == 'I':
            heappush(min_heap, (data,current))
            heappush(max_heap, (-data,current))
            current += 1
    max_value = pop(max_heap)
    if max_value == None:
        print("EMPTY")
    else:
        heappush(min_heap,(-max_value,current))
        print(-max_value,pop(min_heap))