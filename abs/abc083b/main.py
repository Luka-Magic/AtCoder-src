def main():
    n, a, b = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        l = list(map(int, list(str(i))))
        s = sum(l)

        if a <= s <= b:
            ans += i
    print(ans)


if __name__ == '__main__':
    main()
