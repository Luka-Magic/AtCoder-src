import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, x = map(int, input().split())
    low = 0
    high = 10**9 + 1
    while low < high:
        mid = (low + high) // 2
        if mid == low or mid == high:
            break
        value = a * mid + b * (len(str(mid)))
        if value == x:
            break
        if value > x:
            high = mid
        else:
            low = mid
    print(mid)

if __name__ == '__main__':
    main()
