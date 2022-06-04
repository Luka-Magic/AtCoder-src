mod = 10**9 + 7
inf = float('inf')


def main():
    h, w = map(int, input().split())
    masu = [list(input()) for _ in range(h)]
    g = []
    for i in range(h):
        for j in range(w):
            if masu[i][j] == 'o':
                g.append([i, j])
    print(abs(g[0][0] - g[1][0]) + abs(g[0][1] - g[1][1]))
    


if __name__ == '__main__':
    main()
