import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    d, g = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(d)]
    for i in range(2**d):
        ans = 0
        for j in range(d):
            if i << j & 1:
                ans += g




if __name__ == '__main__':
    main()
