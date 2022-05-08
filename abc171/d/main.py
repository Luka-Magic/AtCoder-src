n = int(input())
li = list(map(int, input().split()))

su = sum(li)
from collections import Counter
counter = Counter(li)

q = int(input())

for _ in range(q):
    b, c = map(int, input().split())
    su += (- b + c) * counter[b]
    counter[c] += counter[b]
    counter[b] = 0
    print(su)