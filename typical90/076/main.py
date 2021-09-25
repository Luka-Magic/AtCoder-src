def main():
    n = int(input())
    li = list(map(int, input().split()))
    if (sum(li) % 10 != 0) or (n == 1):
        print('No')
        exit()
    S = sum(li) // 10
    li = li + li
    s = 0
    e = 1
    now = li[0]
    while 1:
        if now == S:
            print('Yes')
            exit()
        if now < S:
            now += li[e]
            e += 1
        elif now > S and e - s > 1:
            now -= li[s]
            s += 1
        elif e - s > 0 or e - s >= n:
            now -= li[s]
            now += li[e]
            e += 1
            s += 1

        if s == 2 * n - 2:
            print('No')
            exit()


if __name__ == '__main__':
    main()
