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
    li = [((k-2) % mod)]
    i = 1
    while i < n-2:
        i *= 2
        li.append(li[-1]**2 % mod)

    ans = k * k-1 % mod
    for i in range(len(li)):
        if (i << (n-2)):
            ans *= (li[i] % mod)
    print(ans % mod)
    # print(li)


if __name__ == '__main__':
    main()

# n, k = map(int, input().split())
# MOD = 1000000007
# print(k if n == 1 else k * (k-1) if n ==
#       2 else k * (k-1) * pow(k-2, n-2, MOD) % MOD)
