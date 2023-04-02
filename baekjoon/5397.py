## 키로거 ##
test_case = int(input())
res = []

for i in range(0,test_case):
    value = input()
    pwd1 = []
    pwd2 = []
    for ch in value:
        if ch == '<':
            if pwd1:
                pwd2.append(pwd1.pop())
        elif ch == '>':
            if pwd2:
                pwd1.append(pwd2.pop())
        elif ch == '-':
            if pwd1:
                pwd1.pop()
        else:
            pwd1.append(ch)
    pwd1.extend(reversed(pwd2))
    res.append(pwd1)

for i in range(len(res)):
    print(''.join(res[i]))
