## 나는 요리사다 ##
per = []
res = []
winner = [0,0]
for i in range(5):
    per.append(list(map(int, input().split())))
    if winner[1] < sum(per[i]):
        winner[0] = i+1
        winner[1] = sum(per[i])

print(' '.join(map(str, winner)))