mod = 998244353
inf = float('inf')


def main():
    t = int(input())

    g = [1]
    for i in range(10**6 + 10):
        g.append(g[-1] * 26 % mod)
    for _ in range(t):
        n = int(input())
        s = list(map(lambda x: ord(x)-65, input()))
        l = (n + 1) // 2
        if n == 1:
            print(s[0]+1)
            continue
        h1 = s[:l]
        h2 = s[-l:][::-1]
        p = 1
        for i1, i2 in zip(h1, h2):
            if i1 == i2:
                continue
            elif i1 < i2:
                p = 1
            else:
                p = 0
        print(
            (sum([g[l-1-i] % mod * k % mod for i, k in enumerate(s[:l])]) + p) % mod)


if __name__ == '__main__':
    main()
