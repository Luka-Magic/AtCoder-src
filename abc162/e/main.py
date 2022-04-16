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
    n, k = map(int, input().split())
    ans = 0
    l = [0] * (k+1)
    for i in range(k, 0, -1):
        c = k // i
        l[i] = pow(c, n, mod)
        # t = 2*i
        # while t <= k:
        #     l[i] -= l[t]
        #     t += i
        if k//i > 1:
            for t in range(2, k//i):
                l[i] -= l[t*i]
    for i, v in enumerate(l):
        ans += (i) * v
        ans %= mod
    print(ans%mod)
    
if __name__ == '__main__':
    main()
