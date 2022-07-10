mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    masu = [list(map(int, list(input()))) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(n):
            for u, r in [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]:
                temp = masu[i][j]
                i_n = i
                j_n = j
                for k in range(n-1):
                    i_n = (i_n + u) % n
                    j_n = (j_n + r) % n
                    temp = temp * 10 + masu[i_n][j_n]
                ans = max(ans, temp)
    print(ans)

if __name__ == '__main__':
    main()
