def main():
    n, l = map(int, input().split())
    k = int(input())
    li = list(map(int, input().split()))

    l_d = [li[0]]
    for i in range(n-1):
        l_d += [li[i+1] - li[i]]
    l_d += [l - li[-1]]

    def f(score):
        now = 0
        i = 0
        c = 0
        for i in range(n+1):
            now += l_d[i]
            if now >= score:
                c += 1
                now = 0
                if c > k:
                    return True
        else:
            return False

    high = l
    low = 0
    score = (high - low) // 2

    while (high - low) > 1:
        if f(score):
            low = score
        else:
            high = score
        score = (high + low) // 2
    print(score)


if __name__ == '__main__':
    main()
