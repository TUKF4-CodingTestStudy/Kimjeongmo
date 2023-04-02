## 해시 알고리즘 ##
from hashlib import sha256

str = input()

res = sha256(str.encode())
print(res.hexdigest())