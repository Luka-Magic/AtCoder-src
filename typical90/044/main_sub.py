import numpy as np


def main():
    n, q = map(int, input().split())
    li = np.array(list(map(int, input().split())))
    for _ in range(q):
        t, x, y = map(int, input().split())
        x, y = x-1, y-1
        if t == 1:
            li[x], li[y] = li[y], li[x]
        elif t == 2:
            li = np.roll(li, 1)
        elif t == 3:
            print(li[x])


if __name__ == '__main__':
    main()
