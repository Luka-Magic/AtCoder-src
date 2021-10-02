import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    s, t = map(int, input().split())
    print(t - s + 1)


if __name__ == '__main__':
    main()
