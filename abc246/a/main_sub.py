import sys
input = sys.stdin.readline


def main():
    x = []
    y = []
    for _ in range(3):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    from collections import Counter
    c = Counter(x)
    d = Counter(y)
    for i, num in c.items():
        if num % 2 == 1:
            x_ = i
    for i, num in d.items():
        if num % 2 == 1:
            y_ = i
    print(x_, y_)


if __name__ == '__main__':
    main()
