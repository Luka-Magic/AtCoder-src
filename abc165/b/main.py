import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    x = int(input())
    ans = 0
    now = 100
    while 1:
        ans += 1
        now = now * 101 // 100
        if now >= x:
            print(ans)
            exit()


if __name__ == '__main__':
    main()
