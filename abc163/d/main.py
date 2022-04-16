import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(k, n+2):
        ans += ((n - i + 1) * i + 1) % mod
        ans %= mod
    print(ans%mod)


if __name__ == '__main__':
    main()
