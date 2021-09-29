import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    ans = 0
    for a in range(1, n):
        b_m = (n-1) // a
        ans += b_m

    print(ans)

if __name__ == '__main__':
    main()
