import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, x = map(int, input().split())
    left = 0
    right = 10**9 + 10
    while right - left != 1:
        mid = (left + right) // 2
        fmid = a * mid + b * (len(str(mid)))
        if fmid <= x:
            left = mid
        else:
            right = mid
    print(min(left, 10**9))

if __name__ == '__main__':
    main()
