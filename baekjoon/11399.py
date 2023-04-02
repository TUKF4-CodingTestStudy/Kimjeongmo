## ATM ##
people = int(input())
time_list = list(map(int, input().split()))
time_list.sort()
num = 0
total_time = 0

for i in range(0,people):
    num += time_list[i]
    total_time += num

print(total_time)