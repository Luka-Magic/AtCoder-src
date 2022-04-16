import math
from functools import reduce
def gcd(*numbers):
    return reduce(math.gcd, numbers)

def prime_factorization(N):  # 素因数分解
    exponent = 0
    while N % 2 == 0:
        exponent += 1
        N //= 2
    if exponent:
        factorization = [[2, exponent]]
    else:
        factorization = []
    i = 1
    while i*i <= N:
        i += 2
        if N % i:
            continue
        exponent = 0
        while N % i == 0:
            exponent += 1
            N //= i
        factorization.append([i, exponent])
    if N != 1:
        factorization.append([N, 1])
    assert N != 0, 'zero'
    return factorization

a, b = map(int, input().split())
print(len(prime_factorization(gcd(a, b)))+1)