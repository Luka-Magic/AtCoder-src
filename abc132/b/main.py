import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1, n-1):
        l = p[i-1:i+2]
        l.sort()
        if l[1] == p[i]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
