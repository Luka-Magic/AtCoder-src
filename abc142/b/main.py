import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    ans = 0
    for l in li:
        if l >= k:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
