import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    g = [[-1]*n for _ in range(n)]
    for i in range(n):
        m = int(input())
        for j in range(m):
            x, y = map(int, input().split())
            g[i][x-1] = y

    ans = 0
    for i in range(2**n):
        l = []
        for j in range(n):
            if (i >> j) & 1:
                l.append(j)
        for a in l:
            for x, y in enumerate(g[a]):
                if y == -1:
                    continue
                elif y == 0:
                    if x in l:
                        break
                elif y == 1:
                    if x not in l:
                        break
            else:
                continue
            break
        else:
            ans = max(ans, len(l))
    print(ans)

if __name__ == '__main__':
    main()
