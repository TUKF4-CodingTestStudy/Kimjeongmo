## 사이클 게임 ##
def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b
        
n,m = map(int, input().split())
parent = [0] * n

for i in range(n):
    parent[i] = i
cycle = False

for i in range(m):
    p1, p2 = map(int, input().split())
    if find(parent,p1) == find(parent,p2):
        cycle = True
        print(i+1)
        break
    else:
        union(parent,p1,p2)
 
if not cycle:
    print(0)    