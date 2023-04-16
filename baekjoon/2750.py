## 수 정렬하기 ##
n = int(input())
ary = []
for _ in range(n):
    ary.append(int(input()))

for i in range(len(ary)):
    print(sorted(ary)[i])