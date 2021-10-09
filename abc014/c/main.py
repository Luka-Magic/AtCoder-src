import sys
from itertools import accumulate

input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

l = [0] * (10 ** 6 + 10)

for a, b in li:
    l[a] += 1
    l[b+1] -= 1

print(max(list(accumulate(l))))