import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')
"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    n = int(input())
    li = list(map(int, input().split()))

    ans = inf
    for i in li:
        k = factorization(i)
        t = 0
        for j, b in k:
            if j == 2:
                t = b
                break
        ans = min(ans, t)
    print(ans)


if __name__ == '__main__':
    main()
