import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li = [10**6] + li + [10**6]
    ans = 0
    for i in range(n):
        ans += min(li[i], li[i+1])
    print(ans)

if __name__ == '__main__':
    main()
