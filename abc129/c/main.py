import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    a = [int(input()) for _ in range(m)]
    a = set(a)
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1 if 1 not in a else 0
    for i in range(2, n+1):
        if i in a:
            continue
        dp[i] = (dp[i-2] + dp[i-1]) % mod
    print(dp[-1] % mod)


if __name__ == '__main__':
    main()
