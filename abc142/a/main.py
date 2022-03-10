import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    print((n//2)/n if n % 2 == 0 else (n//2 + 1)/n)


if __name__ == '__main__':
    main()