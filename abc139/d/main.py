import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    print(n * (n-1) // 2)


if __name__ == '__main__':
    main()
