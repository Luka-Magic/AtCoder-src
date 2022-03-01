import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    su = sum(a)
    t = x // su
    ans = n * t
    no = x % su
    for k in a:
        ans += 1
        no -= k
        if no < 0:
            break
    print(ans)


if __name__ == '__main__':
    main()
