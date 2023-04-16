## 공유기 설치 ##
n, c = map(int, input().split())
div = n/3

home = []
for _ in range(n):
    home.append(int(input()))

home.sort()

start = home[1] - home[0]
end = home[-1] - home[0]

while(start <= end):
    mid = (start + end) // 2 
    val = home[0]
    cnt = 1
    for i in range(1,len(home)):
        if home[i]-val >=  mid:
            val = home[i]
            cnt += 1
    if cnt >= c:
        start = mid + 1
        res = mid
    else:
        end = mid-1
print(res)

# if c > search(home):
#     max_x = 
        