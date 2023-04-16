## 알파벳 찾기 ##

## 내 풀이 ##
import string

letters = list(string.ascii_lowercase)

word = input()

dict = {char:'-1' for char in letters}
    
for ch in word:
    dict[ch] = str(word.index(ch))

print(' '.join(dict.values()))

## 정답 ##
arr = [-1] * 26
data = input().strip()

for i in range(len(data)):
    index = ord(data[i]) -  ord('a')
    if arr[index] == -1:
        arr[index] = i

for x in arr:
    print(x, end=' ')
