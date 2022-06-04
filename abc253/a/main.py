import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c = map(int, input().split())
    if (a <= b and b <= c) or (c <= b and b <= a):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
