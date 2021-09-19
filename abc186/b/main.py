import sys
input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(h)]
    min_ = min([min(i) for i in li])
    sum_ = sum([sum(i) for i in li])
    s = h * w
    print(sum_ - min_ * s)


if __name__ == '__main__':
    main()
