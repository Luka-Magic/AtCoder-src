import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    ans = li[0]
    for i in range(n-1):
        ans = (ans + li[i+1]) / 2
    print(ans)


if __name__ == '__main__':
    main()
