import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans = [-1] * n
    for i in range(n):
        ans[li[i]-1] = i+1
    print(*ans)


if __name__ == '__main__':
    main()
