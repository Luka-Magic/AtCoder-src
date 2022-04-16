from functools import reduce
import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


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

def main():
    a, b = map(int, input().split())
    a_s = set([])
    b_s = set([])
    A = prime_factorization(a)
    B = prime_factorization(b)
    for i, _ in A:
        a_s.add(i)
    for i, _ in B:
        b_s.add(i)
    ans = a_s & b_s

    print(len(ans) + 1)

if __name__ == '__main__':
    main()