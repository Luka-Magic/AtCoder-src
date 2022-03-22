
import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, x = map(int, input().split())
    for d in range(1, 20):
        p = int((x - d * b) // a)
        if 10**d > p:
            print(max(min(p, 10**9), 0))
            exit()


if __name__ == '__main__':
    main()
