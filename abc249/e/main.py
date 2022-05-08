import sys
input = sys.stdin.readline

inf = float('inf')




def main():
    n, p = map(int, input().split())
    N_top = 10**4  # nの上限を先に計算
    mod = p
    g1 = [1, 1]  # 元テーブル
    g2 = [1, 1]  # 逆元テーブル
    inverse = [0, 1]  # 逆元テーブル計算用テーブル
    for i in range(2, N_top + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod//i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)
    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n-r)
        return g1[n] * g2[r] * g2[n-r] % mod
    if n <= 2:
        print(0)
        exit()
    ans = 0
    C = (n - 1) % p
    s25 = 1
    for i in range((n - 1)//2):
        print(i, cmb(n-1, i, p), s25)
        ans += cmb(n-1, i, p) * s25 * 26
        ans %= p
        s25 = s25 * 25
        s25 %= p
    print((ans) % p)

        


if __name__ == '__main__':
    main()
