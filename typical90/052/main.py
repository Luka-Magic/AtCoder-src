def main():
    mod = 10**9 + 7
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    cli = []
    for l in li:
        cli.append(sum(l))
    ans = 1
    for i in cli:
        ans *= i % mod
    print(ans % mod)


if __name__ == '__main__':
    main()
