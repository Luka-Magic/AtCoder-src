import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    ans = float('inf')
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            a = i
            b = n // i
            ans = min(ans, a-1 + b-1)
    print(ans)


if __name__ == '__main__':
    main()