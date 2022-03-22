mod = 10**9 + 7
inf = float('inf')


def main():
    s = input()
    n = len(s)
    p = n // 2
    ans = 0
    for i in range(p):
        if s[i] != s[n-i-1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()