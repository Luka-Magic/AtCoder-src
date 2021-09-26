import math
mod = 10**9 + 7


def main():
    n, k = map(int, input().split())
    if n == 1:
        print(k)
        exit()
    if n == 2:
        print(k * (k-1))
        exit()

    m = int(math.log2(n-2))

    ans = k * (k-1) % mod
    p = (k - 2) % mod
    for i in range(m+1):
        if ((n - 2) >> i) & 1:
            ans *= p % mod
        p = p**2 % mod
    print(ans % mod)


if __name__ == '__main__':
    main()
