import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    g = [[0]*10 for _ in range(10)]
    for i in range(1, n+1):
        p = str(i)
        g[int(p[0])][int(p[-1])] += 1
    ans = 0
    for i in range(10):
        for j in range(10):
            ans += g[i][j] * g[j][i]
    print(ans)

if __name__ == '__main__':
    main()
