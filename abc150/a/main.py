import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    k, x = map(int, input().split())
    print('Yes' if 500 * k >= x else 'No')


if __name__ == '__main__':
    main()
