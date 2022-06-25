import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    m = int(input())
    li = [list(map(int, input().split())) for _ in range(m)]
    n = int(input())
    stars = [tuple(map(int, input().split())) for _ in range(n)]
    stars = set(stars)

    x0, y0 = li[0]

    for i, (sx, sy) in enumerate(stars):
        dx, dy = sx - x0, sy - y0
        for j, (x, y) in enumerate(li):
            if (x + dx, y + dy) not in stars:
                break
        else:
            print(dx, dy)
            exit()

if __name__ == '__main__':
    main()
