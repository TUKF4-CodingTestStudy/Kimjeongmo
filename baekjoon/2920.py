num_list = list(map(int, input().split()))

## 내 풀이 ##
a = sorted(num_list)
b = sorted(num_list,reverse=True)

if num_list == a:
    print("ascending")
elif num_list == b:
    print("descending")
else:
    print("mixed")
    
## 답안 풀이 ##
ascending = True
descending = True

for i in range(1,8):
    if num_list[i] > num_list[i-1]:
        descending = False
    elif num_list[i] < num_list[i-1]:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")