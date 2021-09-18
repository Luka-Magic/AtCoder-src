import sys
input = sys.stdin.readline


def main():
    n, l = map(int, input().split())
    k = int(input())
    Li = list(map(int, input().split()))

    li = [Li[0]] + [Li[i+1] - Li[i] for i in range(len(Li)-1)] + [l - Li[-1]]
    # print(li)

    # 分割できるかどうかの判定
    def f(score):
        su = 0
        t = 0
        for l in li:
            su += l
            if su >= score:
                su = 0
                t += 1
            if t > k:
                flag = True
                break
        else:
            flag = False
        return flag

    low, high = 0, l
    score = l // 2

    while high - low > 1:
        # print(score)
        if f(score):
            low = score
        else:
            high = score
        score = (high + low) // 2
    print(score)


if __name__ == '__main__':
    main()
