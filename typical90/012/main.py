import sys
input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    q = int(input())

    masu = [[0] * w for _ in range(h)]

    for _ in range(q):
        i, *qu = map(int, input().split())
        if i == 1:
            r, c = qu
            masu[c][r] = 1
        else:
            ra, ca, rb, cb = qu
            if (masu[ca][ra] == 0) or (masu[cb, rb] == 0):
                print('No')
                continue


if __name__ == '__main__':
    main()
