import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    if n != 12:
        print(n+1)
    else:
        print(1)


if __name__ == '__main__':
    main()
