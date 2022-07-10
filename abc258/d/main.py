import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, x = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    ans = inf
    temp = 0
    for i, (a, b) in enumerate(li):
        if i == x:
            break
        ans = min(ans, temp + a + b + (b * (x - i - 1)))
        temp += a + b
    print(ans)

if __name__ == '__main__':
    main()
