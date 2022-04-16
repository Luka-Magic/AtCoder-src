import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    ans = n - sum([i for i in li])
    print(ans if ans >= 0 else -1)


if __name__ == '__main__':
    main()
