import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def main():
    n, m, k = map(int, input().split())
    masu = [[0] * m for _ in range(n)]
    max_ = m
    for i in range(m):
        masu[0][i] = i + 1
    for i in range(1, n):
        for j in range(m):
            if j - k >= 0:
                masu[i][j] += masu[i-1][j-k]
                masu[i][j] %= mod
            if j + k <= m:
                masu[i][j] += max_ - masu[i-1][j+k-1]
                masu[i][j] %= mod
            if j != 0:
                masu[i][j] += masu[i][j-1]
                masu[i][j] %= mod
        max_ = masu[i][m-1]
    print(masu[-1][-1] % mod)

if __name__ == '__main__':
    main()
