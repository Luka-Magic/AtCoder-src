from bisect import bisect
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    def f(a, b):
        return a**3 + a**2 * b + a * b**2 + b**3
    

if __name__ == '__main__':
    main()
