## 풍선 터뜨리기 ##
from collections import deque

n = int(input())
num = list(map(int, input().split()))
res = []
dq = deque([i for i in range(1,n+1)])


for _ in range(n):
    res.append(str(dq[0]))
    pt = num[dq[0]-1]
    dq.popleft()
    if dq:
        if pt > 0:
            for _ in range(pt-1):
                dq.append(dq.popleft())
        else:
            for _ in range(-pt):
                dq.appendleft(dq.pop())

print(' '.join(res))