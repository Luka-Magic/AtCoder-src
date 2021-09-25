def main():
    q = int(input())
    up = []
    u = 0
    down = []
    d = 0
    for _ in range(q):
        t, x = map(int, input().split())
        if t == 1:
            up.append(x)
            u += 1
        elif t == 2:
            down.append(x)
            d += 1
        else:
            if x <= u:
                print(up[-x])
            else:
                print(down[x-u-1])


if __name__ == '__main__':
    main()
