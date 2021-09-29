import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    x, y = map(int, input().split('.'))
    if y <= 2:
        print(str(x) + '-')
    elif y <= 6:
        print(str(x))
    else:
        print(str(x) + '+')


if __name__ == '__main__':
    main()
