import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    t = list(input())
    di = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    now = 0
    x, y = 0, 0
    for p in t:
        if p == 'S':
            x_, y_  = di[now]
            x += x_
            y += y_
        else:
            now += 1
            now %= 4
    print(x, y)

if __name__ == '__main__':
    main()
