import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, x = map(int, input().split())
    import math
    S = x / a
    if S > (a * b / 2):
        k = (2*a*b - 2*S) / (a*a)
    else:
        k = (b*b) / (2*S)
    print(math.degrees(math.atan(k)))


if __name__ == '__main__':
    main()
