mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    # print(2**15)
    li = [input() for _ in range(n)]
    ans = 0

    from collections import Counter

    for i in range(2**n):
        s = ''
        temp_ans = 0
        for j in range(n):
            if (i >> j) & 1:
                s += li[j]
        c = Counter(s)
        for i in c.values():
            if i == k:
                temp_ans += 1
        ans = max(ans, temp_ans)
    print(ans)


if __name__ == '__main__':
    main()
