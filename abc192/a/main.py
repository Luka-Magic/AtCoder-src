import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    print(100 - (n % 100))


if __name__ == '__main__':
    main()
