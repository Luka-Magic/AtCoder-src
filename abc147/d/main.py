import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def ten2n(num_10, n):
    str_n = ''
    while num_10:
        if num_10 % n >= 10:
            return -1
        str_n += str(num_10 % n)
        num_10 //= n
    return (str_n[::-1]).zfill(61)

def main():
    n = int(input())
    li = list(map(lambda x: ten2n(int(x), 2), input().split()))
    ans = 0
    for k in range(61):
        k_d = 0
        for i in li:
            if i[-k-1] == '1':
                k_d += 1
        ans += k_d * (n-k_d) * (2 ** k)
        ans %= mod
    print(ans)


if __name__ == '__main__':
    main()
