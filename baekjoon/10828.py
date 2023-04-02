## 스택 ##

n = int(input())
stack = []
res = []
for i in range(n):
    command = input()
    if command.startswith("push"):
        stack.append(command.split()[1])
    elif command == "pop":
        if stack:
            res.append(stack.pop())
        else:
            res.append('-1')
    elif command == "size":  
        res.append(len(stack))
    elif command == "empty":
        if not stack:
            res.append('1')
        else:
            res.append('0')
    elif command == "top":
        if not stack:
            res.append('-1')
        else:
            res.append(stack[-1])
        
for i in res:
    print(i)