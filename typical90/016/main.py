def main():
    n = int(input())
    a, b, c = map(int, input().split())

    ans = 10000

    for i in range(10000):
        for j in range(10000 - i):
            k = n - (a * i + b * j)
            if k < 0:
                continue
            if k % c == 0:
                ans = min(ans, k//c + i + j)
    print(ans)


if __name__ == '__main__':
    main()
