def main():
    n, m, t = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(m)]

    now = 0
    bat = n
    for a, b in li:
        bat -= (a - now)
        if bat <= 0:
            print('No')
            exit()
        bat += (b - a)
        bat = min(n, bat)
        now = b
    if bat - (t - now) <= 0:
        print('No')
        exit()
    print('Yes')


if __name__ == '__main__':
    main()
