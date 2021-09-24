import sys
input = sys.stdin.readline


def main():
    h, w = map(int, input().split())
    masu = [list(map(int, input().split())) for _ in range(h)]
    ans = [[0]*w for _ in range(h)]
    h_li = []
    w_li = []

    for i in range(h):
        h_li.append(sum(masu[i]))

    for j in range(w):
        w_li_ = 0
        for i in range(h):
            w_li_ += masu[i][j]
        w_li.append(w_li_)

    for i in range(h):
        for j in range(w):
            ans[i][j] = h_li[i] + w_li[j] - masu[i][j]
    
    for row in ans:
        print(*row)

if __name__ == '__main__':
    main()