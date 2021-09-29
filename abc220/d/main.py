import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    l = [[0] * 10 for _ in range(n)]
    l[0][li[0]] = 1

    for i, k in enumerate(li[1:]):
        i += 1
        # print(i)
        for j in range(10):
            if l[i-1][j] != 0:
                a = (k + j) % 10
                b = (k * j) % 10
                l[i][a] += l[i-1][j] % mod
                l[i][b] += l[i-1][j] % mod
    ans = [i % mod for i in l[-1]]
    print(*ans, sep='\n')


if __name__ == '__main__':
    main()
