n = int(input())
li = list(map(int, input().split()))

li.sort()

from collections import Counter
c = Counter(li)
ans = 0
for i in range(1, (2*10**5 + 1)):
    for j in range(1, (2*10**5 + 1) // i + 10):
        ans += c[i] * c[j] * c[i*j]
print(ans)