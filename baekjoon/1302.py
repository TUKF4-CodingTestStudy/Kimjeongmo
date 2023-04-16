## 베스트셀러 ##
from collections import Counter

n = int(input())
books = []
    
def get_most_common(strings):
    # Counter를 사용하여 각 문자열의 등장 횟수를 카운트
    counts = Counter(strings)
    
    # 가장 많이 등장한 문자열들을 저장
    most_common = []
    
    # Counter의 most_common 메소드를 사용하여 등장 횟수가 가장 많은 문자열과 그 등장 횟수를 가져옴
    max_count = counts.most_common(1)[0][1]
    
    # 등장 횟수가 가장 많은 문자열들을 most_common 리스트에 저장
    for string, count in counts.items():
        if count == max_count:
            most_common.append(string)
    
    # 문자열들을 사전순으로 정렬하고 가장 첫 번째 값을 반환
    return sorted(most_common)[0]

for _ in range(n):
    books.append(input())

print(get_most_common(books))