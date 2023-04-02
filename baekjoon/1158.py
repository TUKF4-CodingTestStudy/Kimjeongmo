## 요세푸스 문제 ##
from collections import deque
n,k = list(map(int,input().split()))
dq = deque([i+1 for i in range(n)])

res = []
pt = k-1
while(dq):
    for i in range(k-1):
        dq.append(dq.popleft())
    res.append(dq.popleft())

print("<" + ", ".join(str(i) for i in res) + ">")