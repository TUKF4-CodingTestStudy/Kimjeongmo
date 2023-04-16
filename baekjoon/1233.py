## 주사위 ##
s1,s2,s3 = map(int, input().split())

## 딕셔너리 초기화 ##
res = dict()

## 주사위 3개 합 반복문으로 더하기 ##
## 이미 있으면 카운트 +1 , 없으면 1로 초기화 ##
for i in range(1,s1+1):
    for j in range(1,s2+1):
        for k in range(1,s3+1):
            if res.get(i+j+k):
                res[i+j+k] += 1
            else:
                res[i+j+k] = 1
            
## 최대 카운트값 검색 ##            
print(max(res, key=res.get))

