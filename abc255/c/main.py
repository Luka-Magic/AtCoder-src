import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    x, a, d, n = map(int, input().split())

    if (x <= a and d >= 0):
        print(abs(a - x))
    elif (a + d * (n-1) >= x and d <= 0):
        print((a + d * (n-1)) - x)
    elif (x >= a and d <= 0):
        print(x - a)
    elif (a + d * (n-1) <= x and d >= 0):
        print(x - (a + d * (n-1)))
    elif d > 0:
        p = x - a
        p %= d
        print(min(abs(p), abs(p-d)))
    elif d < 0:
        p = x - a
        p %= d
        print(min(abs(p), abs(p-d)))
    elif d == 0:
        print(abs(a - x))



if __name__ == '__main__':
    main()
