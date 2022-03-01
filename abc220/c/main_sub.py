import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    x = int(input())
    s = sum(li)
    ans = n * (x // s)
    t = s * (x // s)
    while t <= x:
        t += li[ans % n]
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
