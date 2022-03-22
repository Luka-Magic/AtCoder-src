import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    v, a, b, c = map(int, input().split())
    v %= (a+b+c)
    v -= a
    if v < 0:
        print('F')
        exit()
    v -= b
    if v < 0:
        print('M')
    else:
        print('T')


if __name__ == '__main__':
    main()
