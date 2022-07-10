mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    s = list(map(int, list(input())))
    li = list(map(int, input().split()))
    p = [[i, j] for i, j in zip(li, s)]
    p.sort(key=lambda x: x[0])
    now = sum(s)
    ans = max(now,  n - now)
    for i in range(n-1):
        if p[i][1] == 0:
            now += 1
        else:
            now -= 1
        if p[i][0] == p[i+1][0]:
            continue
        ans = max(ans, now)
    print(ans)

if __name__ == '__main__':
    main()
