import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, k = map(int, input().split())
    ans = 0
    while 1:
        if b <= a:
            print(ans)
            exit()
        else:
            ans += 1
            a *= k

if __name__ == '__main__':
    main()
