import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dp = [[-1]*2 for _ in range(n)]
    dp[0][0], dp[0][1] = 1, 1
    for i in range(1, n):
        if 

if __name__ == '__main__':
    main()
