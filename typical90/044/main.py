def main():
    n, q = map(int, input().split())
    li = list(map(int, input().split()))
    roll = 0
    for _ in range(q):
        t, x, y = map(int, input().split())
        i, j = (x-1-roll) % n, (y-1-roll) % n
        if t == 1:
            li[i], li[j] = li[j], li[i]
        elif t == 2:
            roll += 1
        else:
            print(li[i])


if __name__ == '__main__':
    main()
