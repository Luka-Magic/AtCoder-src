from collections import Counter as C


def main():
    n = int(input())
    a_ = list(map(int, input().split()))
    b_ = list(map(int, input().split()))
    c_ = list(map(int, input().split()))

    a__ = [i % 46 for i in a_]
    b__ = [i % 46 for i in b_]
    c__ = [i % 46 for i in c_]

    a = C(a__)
    b = C(b__)
    c = C(c__)

    ans = 0

    for i in range(46):
        for j in range(46):
            for k in range(46):
                if (i + j + k) % 46 == 0:
                    ans += a[i] * b[j] * c[k]
    print(ans)


if __name__ == '__main__':
    main()
