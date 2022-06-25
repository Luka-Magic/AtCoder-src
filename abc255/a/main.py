import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    r, c = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(2)]
    print(li[r-1][c-1])


if __name__ == '__main__':
    main()
