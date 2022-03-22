import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def primes(n):
    prime = [True for i in range(n+1)]
    prime[0], prime[1] = False, False
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime


def main():
    x = int(input())
    p = primes(10**7)
    for i in range(x, 10**7):
        if p[i]:
            print(i)
            exit()

if __name__ == '__main__':
    main()
