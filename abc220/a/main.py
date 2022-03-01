import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c = map(int, input().split())
    x = (b // c) * c
    if x >= a:
        print(x)
    else:
        print(-1)


if __name__ == '__main__':
    main()
