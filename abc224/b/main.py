import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    h, w = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(h)]

    for i1 in range(h):
        for i2 in range(i1+1, h):
            for j1 in range(w):
                for j2 in range(j1+1, w):
                    if li[i1][j1] + li[i2][j2] > li[i1][j2] + li[i2][j1]:
                        print('No')
                        exit()
    print('Yes')


if __name__ == '__main__':
    main()
