def main():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        g[a-1].append(b-1)
        g[b-1].append(a-1)
    ans = 0
    for i, l in enumerate(g):
        k = 0
        for j in l:
            if i > j:
                k += 1
        if k == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
