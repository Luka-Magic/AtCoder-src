def main():
    n = int(input())
    k = int(input())
    ans = 1
    for i in range(n):
        if 2**i < k:
            ans *= 2
        else:
            ans += k
    print(ans)


if __name__ == '__main__':
    main()
