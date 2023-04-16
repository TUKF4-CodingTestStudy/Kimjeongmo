## 0만들기 ##
test_case = int(input())
num = []
oper = [' ','+','-']
for _ in range(test_case):
    n = int(input())
    
    [num.append(i) for i in range(1,n+1)]
    for operator in oper:
        val = ""
        for i in range(len(num)-1):
            val += str(num[i]) + oper[i]
        val += str(num[-1])
        
        