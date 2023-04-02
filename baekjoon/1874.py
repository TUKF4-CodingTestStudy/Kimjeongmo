## 스택 수열 ##
n = int(input())
stack = [] 
res = []
pt = 1
for i in range(0,n):
    a = int(input())
    while pt <= a:
        stack.append(pt)
        res.append('+')
        pt += 1
    if stack[-1] == a:
        stack.pop()
        res.append('-')
    else:
        print('NO')
        exit(0)
        

for data in res:
    print(data)

