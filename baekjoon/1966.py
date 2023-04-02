## 프린터 큐 ##

test_case = int(input())
res = []
for i in range(0,test_case):
    n, m = list(map(int, input().split()))
    rate = list(map(int, input().split()))
    rate = [(i, idx) for idx, i in enumerate(rate)]
    cnt = 0

    
    while True:
        if rate[0][0] == max(rate, key=lambda x: x[0])[0]:
            cnt += 1
            if rate[0][1] == m:
                res.append(cnt)
                break
            else:
                rate.pop(0)
        else:
            rate.append(rate.pop(0))


for i in range(len(res)):
    print(res[i])
   

 
