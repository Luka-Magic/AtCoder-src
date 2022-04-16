import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, m, x = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    ans = inf
    for i in range(2**n):
        value = 0
        li_ = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                value += li[j][0]
                for k in range(m):
                    li_[k] += li[j][k+1]
        for k in range(m):
            if li_[k] < x:
                break
        else:
            ans = min(ans, value)
    print(ans if ans != inf else -1)

if __name__ == '__main__':
    main()
