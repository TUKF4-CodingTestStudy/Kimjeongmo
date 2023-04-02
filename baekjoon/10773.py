## 제로 ##
n = int(input())
res = []

for i in range(n):
    num = int(input())
    if num != 0:
        res.append(num)
    else:
        res.pop()

print(sum(res))