import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, q = map(int, input().split())
    s = list(input())
    start = 0
    for _ in range(q):
        i, x = map(int, input().split())
        if i == 1:
            start += x
            start %= n
        elif i == 2:
            print(s[(-start + x - 1) % n])


if __name__ == '__main__':
    main()
