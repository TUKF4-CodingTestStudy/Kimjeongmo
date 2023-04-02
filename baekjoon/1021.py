## 회전하는 큐 ##
from collections import deque

n, m = list(map(int,input().split()))
list = list(map(int,input().split()))
stack = ([i+1 for i in range(n)])
cnt = 0

# for data in list:
#     distance = stack.index(data)
#     while(data != stack[0]):
#         if distance >= len(stack)-distance:
#             stack.insert(0,stack.pop())
#             cnt += 1
#         elif distance < len(stack)-distance:
#             stack.append(stack.pop(0))
#             cnt += 1
#     stack.pop(0)
# print(cnt)

dq = deque([i+1 for i in range(n)])

for data in list:
    distance = dq.index(data)
    while(data != dq[0]):
        if distance >= len(dq)-distance:
            dq.appendleft(dq.pop())
            cnt += 1
        elif distance < len(stack)-distance:
            dq.append(dq.popleft())
            cnt += 1
    dq.popleft()
print(cnt)