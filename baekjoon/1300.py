## k번째 수 ##
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 0, k
cnt = 0


## 이분탐색 활용
## mid값보다 작은 수의 갯수(cnt), k값 비교
## cnt >= k 면 찾은거
## cnt < k면 mid가 더 커야하기 때문에 start를 mid+1로 바꾸고 다시 찾기

while start <= end:
    mid = (start+end) // 2
    ## cnt는 mid보다 작은 수의 갯수
    cnt = 0

    for i in range(1,n+1):
        ## mid//i가 n보다 크면 안되니까 최댓값은 n
        cnt += min(mid//i, n)  
        
    ## cnt가 찾는 k랑 같아지면 answer
    if cnt >= k:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)