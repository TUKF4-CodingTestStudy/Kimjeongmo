## 좌표 정렬하기 ##
n = int(input())
ary = []
for _ in range(n):
    x, y = map(int,input().split())
    ary.append([x,y])
sorted_ary = sorted(ary)

for i in range(len(sorted_ary)):
    print(sorted_ary[i][0],sorted_ary[i][1])