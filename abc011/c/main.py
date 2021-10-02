import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    ng = [int(input()) for _ in range(3)]

    dp = [inf] * (n + 1)
    if n in ng:
        print('NO')
        exit()
    dp[n] = 0
    if n-1 not in ng:
        dp[n-1] = 1
    if n-2 not in ng and n > 1:
        dp[n-2] = 1
    if n <= 2:
        if dp[0] <= 100:
            print('YES')
        else:
            print('NO')
        exit()

    for i in range(n-3, -1, -1):
        if i in ng:
            continue
        dp[i] = min(dp[i+1]+1, dp[i+2]+1, dp[i+3]+1)

    if dp[0] <= 100:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
