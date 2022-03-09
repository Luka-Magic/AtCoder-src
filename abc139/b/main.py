import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')
import math


def main():
    a, b = map(int, input().split())
    print(math.ceil((b-a) / (a-1) + 1))


if __name__ == '__main__':
    main()
