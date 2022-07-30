from itertools import accumulate
import sys
input = sys.stdin.readline


mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    # bo: カウンタがi (0~N)のときにもらえるボーナス
    bo = [0] * (n + 1)
    for _ in range(m):
        i, v = map(int, input().split())
        bo[i] = v

    # dp[i][c]: i回目でカウンタがcのとき、それ以降でもらえる最大のお金
    # 後ろから考える
    dp = [[0]*(n+2) for _ in range(n+1)]
    for i in range(n-1, -1, -1):
        for c in range(i+2):
            dp[i][c] = max(dp[i+1][0], dp[i+1][c+1])
            if c != 0:
                dp[i][c] += bo[c] + li[i]

    print(max(dp[0]))


if __name__ == '__main__':
    main()
