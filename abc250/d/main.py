import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


import math
def prime_enumeration(n):
    prime = [True for i in range(n+1)]
    prime[0], prime[1] = False, False
    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    return prime

def main():
    n = int(input())
    prime = prime_enumeration(10**6)
    li = [i for i, p in enumerate(prime) if p]
    ans = 0
    for i, q in enumerate(li):
        low = -1
        high = i
        while low+1 < high:
            mid = (low + high) //2
            p = li[mid]
            value = p * q ** 3
            if n < value:
                high = mid
            else:
                low = mid
        ans += low+1
    print(ans)

if __name__ == '__main__':
    main()
