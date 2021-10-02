mod = 10**9 + 7
inf = float('inf')


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
    li = [int(input()) for _ in range(n)]
    num_li = []
    ans = 0
    s = 1
    for i in range(1, n+1):
        s *= i

    for p, i in enumerate(li):
        num = 0
        for q, j in enumerate(li):
            if p == q:
                continue
            if i % j == 0:
                num += 1
        num_li.append(num)

    k = 0
    for num in num_li:
        p = (num // 2) + 1
        q = num + 1
        k += (s * p) // q
    print(k / s)


if __name__ == '__main__':
    main()
