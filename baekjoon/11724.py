## 연결 요소의 개수 ##

import sys

sys.setrecursionlimit(5000)


n,m = map(int, input().split())
visited = [False] * (1+n)
ary = [[] for i in range(n)]
cnt = 0

## depth로 디버깅할때 확인 ##
def dfs(start, depth):
    visited[start] = True
    for i in ary[start]:
        if not visited[i]:
            dfs(i, depth+1)
    

for _ in range(m):
    u, v = map(int, input().split())
    ary[u-1].append(v-1)
    ary[v-1].append(u-1)
    

for i in range(n):
    if not visited[i]:
        if not ary[i]:
            cnt += 1
            visited[i] = True
        else:
            dfs(i, 0)
            cnt += 1

        
print(cnt)
