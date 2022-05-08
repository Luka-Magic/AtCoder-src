import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    ans = 4
    h, w = map(int, input().split())
    r, c = map(int, input().split())
    if r == h:
        ans -= 1
    if r == 1:
        ans -= 1
    if c == w:
        ans -= 1
    if c == 1:
        ans -= 1
    print(ans)


if __name__ == '__main__':
    main()
