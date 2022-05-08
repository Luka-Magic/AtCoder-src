import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

N_top = 10**4 # nの上限を先に計算
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

def main():
    s = int(input())
    max_k = s // 3
    ans = 0
    for k in range(1, max_k+1):
        ans += cmb(s-2*k-1, k-1, mod)
        ans %= mod
    print(ans%mod)

if __name__ == '__main__':
    main()