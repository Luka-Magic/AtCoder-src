import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    li.sort()
    from collections import Counter
    c = Counter(li)
    for a in li:
        insu = make_divisors(a)
        # print(a, insu)
        for i in insu:
            j = i
            k = a // j
            # if a == j and j == k:
            #     temp_ans = c[j] * c[k]
            # else:
            temp_ans = c[j] * c[k]
            # print(a, j, k, temp_ans)
            ans += temp_ans
    print(ans)


if __name__ == '__main__':
    main()
