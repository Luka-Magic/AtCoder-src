import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    r, s, p = map(int, input().split())
    t = list(input())
    janken = ['r', 's', 'p']
    for j in range(k):
        dp = [[0]*3 for _ in range((n-j+2)//k+1)]
        for i, h in enumerate(range(j, n, k)):
            for v, pre in enumerate(janken):
                aite = t[h]
                dp[i+1][v] = max([dp[i][q] for q in range(3)])
                if aite == 'r':
                    if pre == 'p':
                        dp[i+1][v] = 0
                    else:
                        dp[i+1][v] = p
                if aite == 's':
                    if pre == 'r':
                        dp[i+1][v] = 0
                    else:
                        dp[i+1][v] = r
                if aite == 'p':
                    if pre == 's':
                        dp[i+1][v] = 0
                    else:
                        dp[i+1][v] = s


if __name__ == '__main__':
    main()