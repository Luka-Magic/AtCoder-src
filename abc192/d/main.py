import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def f(x, base):
    x = list(map(int, list(str(x))))
    num = 0
    for i in x:
        num = num * base + i
    return num


def main():
    X = int(input())
    m = int(input())
    t = max(list(map(int, list(str(X)))))
    if X < 10:
        print(+(X <= m))
        exit()

    low, high = t, m+1

    while high - low > 1:
        mid = (high + low) // 2
        x = f(X, mid)
        if x > m:
            high = mid
        else:
            low = mid
    print(low - t)


if __name__ == '__main__':
    main() 
