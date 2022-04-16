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
    n = int(input())
    li = prime_factorization(n)
    ans_li = []
    for v, c in li:
        temp = 1
        while 1:
            c -= temp
            if c < 0:
                break
            ans_li.append(v**temp)
            temp += 1
    ans_li.sort()
    ans = 0
    for i in ans_li:
        if n < i:
            break
        ans += 1
        n //= i
    print(ans)






    # print(prime_factorization(n))


if __name__ == '__main__':
    main()
