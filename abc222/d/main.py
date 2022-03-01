mod = 998244353
inf = float('inf')


def main():
    n = int(input())
    li = [[0] * n for _ in range(3001)]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(a[0], b[0]+1):
        li[i][0] = 1

    for i in range(1, n):
        for j in range(a[i], b[i] + 1):
            if j == a[i]:
                for k in range(a[i]+1):
                    li[j][i] += li[k][i-1] % mod
            else:
                li[j][i] += li[j-1][i] + li[j][i-1] % mod
            li[j][i] %= mod
    
    ans = 0
    for i in range(3001):
        ans += li[i][n-1] % mod
    print(ans % mod)


if __name__ == '__main__':
    main()
