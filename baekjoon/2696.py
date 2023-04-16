## 중앙값 구하기 ##
t = int(input())
cnt_res = []
val_res = []
for _ in range(t):
    res = []
    cnt = 0
    m = int(input())
    ary = []
    for _ in range(m // 10 + 1):
        ary += list(map(int, input().split()))
    
    ## 인덱스 번호가 홀수일때마다 
    ## 해당 인덱스까지 배열을 잘라서 내림차순 정렬하고 
    ## 중앙값 검색
    for i in range(1,len(ary)+1):
        if i%2 == 1:
            sort_ary = sorted(ary[:i], reverse=True) 
            res.append(sort_ary[i//2:i//2+1][0])
            cnt += 1
            
    print(cnt)
    for data in res:
        print(data, end=' ')
    print()


## 블로그 참조 ##

# T = int(input())
# for _ in range(T):
#     M = int(input())
#     nums = []
#     for _ in range(M // 10 + 1):
#         nums += list(map(int, input().split()))

#     print(M // 2 + 1)
#     for i in range(1, len(nums) + 1, 2):
#         print(sorted(nums[:i])[i // 2], end=' ')
#     print()