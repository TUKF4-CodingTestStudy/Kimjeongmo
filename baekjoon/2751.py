## 수 정렬하기 2 ##
import sys
input = sys.stdin.readline
n = int(input())
ary = []
for _ in range(n):
    ary.append(int(input()))
    
for i in sorted(ary):
    print(i)