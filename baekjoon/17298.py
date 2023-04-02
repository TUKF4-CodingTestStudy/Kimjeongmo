## 오큰수 ##
a = int(input())
list = list(map(int,input().split()))
n = 0
NGE = [-1] * a
res = []
stack = []
max = max(list)

# for i in range(len(list)):
    # if i+n < len(list)-1:
    #     while(list[i]>=list[i+n]):
    #         n += 1  
    #     res.append(list[i+n])
    #     n=0
    # else:
    #     res.append(-1)


for i in range(a):
    if len(stack) == 0 or stack[-1][0] >= list[i]:
        stack.append((list[i],i))
    else:
        while len(stack) > 0:
            previous, index = stack.pop()
            if previous >= list[i]:
                stack.append((previous,index))
                break
            else:
                NGE[index] = list[i]
        stack.append((list[i],i))        


print(*NGE)
            
# 오른쪽에 없는 경우
