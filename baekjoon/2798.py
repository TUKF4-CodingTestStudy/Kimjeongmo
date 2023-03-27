card_num, num = list(map(int, input().split()))
card_list = list(map(int, input().split()))
length = len(card_list)
res = 0

for i in range(length):
    for j in range(i+1,length):
        for k in range(j+1,length):
            current_sum = card_list[i]+card_list[j]+card_list[k]
            if current_sum <= num:
                res = max(current_sum,res)
                
print(res)

