import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    table = [[0.]*n for _ in range(n)]
    li = [list(map(int, input().split())) for _ in range(n)]
    from itertools import combinations
    def f(x1, y1, x2, y2):
        return (y2 - y1) / (x2 - x1) if x2 != x1 else inf
    for i, j in combinations(list(range(n)), 2):
        p = f(li[i][0], li[i][1], li[j][0], li[j][1])
        table[i][j] = p
        table[j][i] = p
    for l in table:
        print(*l)
        




if __name__ == '__main__':
    main()
