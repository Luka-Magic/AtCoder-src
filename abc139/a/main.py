mod = 10**9 + 7
inf = float('inf')


def main():
    s = list(input())
    t = list(input())
    ans = 0
    for i, j in zip(s, t):
        ans += 1 if i == j else 0
    print(ans)


if __name__ == '__main__':
    main()
