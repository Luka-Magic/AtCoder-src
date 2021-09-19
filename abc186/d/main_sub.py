import sys
input = sys.stdin.readline


def main():
    n = int(input())
    li = list(map(int, input().split()))
    s = sum(li)
    li.sort()
    ans = 0
    t = 0
    for k, i in enumerate(li):
        t += i
        ans += s - t - (i*(n-1-k))
    print(ans)


if __name__ == '__main__':
    main()
