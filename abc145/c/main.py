import math
from itertools import permutations
n = int(input())
s = 0
li = [list(map(int, input().split())) for _ in range(n)]
n_ = 0
for i in permutations(list(range(n)), n):
    temp = 0
    for j in range(1, n):
        x1, y1 = li[i[j-1]]
        x2, y2 = li[i[j]]
        temp += math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    s += temp
    n_ += 1
print(s / n_)
