import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c, x = map(int, input().split())
    if a >= x:
        print(1.)
    elif x <= b:
        print(c / (b - a))
    else:
        print(0.)


if __name__ == '__main__':
    main()
