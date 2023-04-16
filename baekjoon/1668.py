## 트로피 진열 ##
n = int(input())
ary = []
left, right = 0, 0
left_cnt, right_cnt = 0, 0

for _ in range(n):
    ary.append(int(input()))

for tropy in ary:
    if tropy > left:
        left = tropy
        left_cnt += 1

for tropy in ary[::-1]:
    if tropy > right:
        right = tropy
        right_cnt += 1

print(left_cnt)
print(right_cnt)