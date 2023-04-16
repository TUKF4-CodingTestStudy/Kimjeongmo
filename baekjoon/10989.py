## 수 정렬하기 3 ##
import sys
## 데이터의 최댓값이 10000개로 정해져있으므로 계수 정렬 이용
input = sys.stdin.readline
n = int(input())
ary = [0] * 10001
for _ in range(n):
    num = int(input())
    ary[num] += 1

for i in range(len(ary)):
    if ary[i] != 0:
        for _ in range(ary[i]):
            print(i)

