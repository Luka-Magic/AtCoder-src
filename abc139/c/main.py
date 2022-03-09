from mimetypes import init
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    c = 0
    now = li[0]
    for i in range(1, n):
        if li[i] - now <= 0:
            c += 1
            ans = max(ans, c)
        else:
            c = 0
        now = li[i]
    print(ans)
        



if __name__ == '__main__':
    main()
