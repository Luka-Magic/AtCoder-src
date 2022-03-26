import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k, m = map(int, input().split())
    A = list(map(int, input().split()))
    s = sum(A)
    print(max(m * n - s, 0) if m * n - s <= k else -1)

if __name__ == '__main__':
    main()
