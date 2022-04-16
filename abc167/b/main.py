import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c, k = map(int, input().split())
    if a > k:
        print(k)
    elif a <= k < a + b:
        print(a)
    elif a + b <= k <= a + b + c:
        print(a - k + a + b)

if __name__ == '__main__':
    main()
