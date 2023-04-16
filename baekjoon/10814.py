## 나이순 정렬 ##
n = int(input())
ary = []
for i in range(n):
    cmd = input().split()
    age, name = int(cmd[0]), cmd[1]
    ary.append([age,i, name])


sorted_ary = sorted(ary)

for i in range(n):
    print(sorted_ary[i][0], end=" ")
    print(sorted_ary[i][2])
