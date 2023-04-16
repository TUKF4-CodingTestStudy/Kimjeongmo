## 수 찾기 ##

n = int(input())
list1 = set(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
for data in list2:
    if data in list1:
        print('1')
    else:
        print('0')