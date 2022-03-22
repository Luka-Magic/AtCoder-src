
import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, x = map(int, input().split())
    for d in range(1, 11):
        p = (x - d * b) // a
        if 10**d - 1 > p:
            if 10**(d-1) > p:
                ans = 10**(d-1) - 1
            else:
                ans = p
            break
    else:
        print(10**9)
        exit()
    print(min(ans, 10**9))

if __name__ == '__main__':
    main()