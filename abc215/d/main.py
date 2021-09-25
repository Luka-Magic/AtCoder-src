import math
n, m = map(int, input().split())
li = list(map(int, input().split()))


def factorization(i):
    now = i
    primes = set()
    for k in range(2, int(math.sqrt(i))+1):
        if now % k == 0:
            primes.add(k)
            while now % k == 0:
                now //= k
    if now != 1:
        primes.add(now)
    return primes


primes = set()
for i in li:
    p = factorization(i)
    for j in p:
        primes.add(j)
ans_l = [0] + [1] * m
for i in primes:
    for j in range(0, m+1, i):
        ans_l[j] = 0
print(sum(ans_l))
for i, k in enumerate(ans_l):
    if k:
        print(i)
