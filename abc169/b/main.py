import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans = 1
    li.sort()
    for i in li:
        ans *= i
        if ans > 10**18:
            print(-1)
            exit()
    print(ans)

if __name__ == '__main__':
    main()
