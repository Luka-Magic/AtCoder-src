n = int(input())
li = list(map(int, input().split()))
_ = int(input())
M = list(map(int, input().split()))

sums = set()

for i in range(2**n):
    t = 0
    for j in range(n):
        if (i >> j) & 1:
            t += li[j]
    sums.add(t)

for m in M:
    if m in sums:
        print('yes')
    else:
        print('no')