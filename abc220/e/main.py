import sys
input = sys.stdin.readline

mod = 998244353
inf = float('inf')


def main():
    n, d = map(int, input().split())
    ans = 0
    if d == 1:
        ans = 0
        for i in range(n):
            ans += 2 ** (i+1)
        print(ans)
        exit()


if __name__ == '__main__':
    main()


# N, D = map(int, input().split())
# ANS = 0
# mod = 998244353
# x = pow(2, D-1, mod)
# y = pow(2, D, mod)
# z = 1
# for i in range(N-1):
#   if (N-i-1)*2 < D:
#     break
#   ANS += x*min(D-1, (N-i-1)*2-D+1)
#   if i+D < N:
#     ANS += y*2*z
#   ANS %= mod
#   x = x*2 % mod
#   y = y*2 % mod
# print(ANS)
