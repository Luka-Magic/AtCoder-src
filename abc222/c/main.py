import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    li = [list(input()) for _ in range(2*n)]
    l = [[i, 0] for i in range(2*n)]

    for i in range(m):
        for k in range(n):
            a_n = l[k*2][0]
            b_n = l[k*2+1][0]
            judge = janken(a_n, b_n, i, li)
            if judge == 'win':
                l[k*2][1] += 1
            elif judge == 'loss':
                l[k*2+1][1] += 1
        l.sort(key=lambda x: x[0])
        l.sort(key=lambda x: x[1], reverse=True)

    for i, j in l:
        print(i+1)


def janken(i, j, k, li):
    a = li[i][k]
    b = li[j][k]
    if a == 'P' and b == 'G':
        return 'win'
    if a == 'C' and b == 'P':
        return 'win'
    if a == 'G' and b == 'C':
        return 'win'
    if a == 'P' and b == 'C':
        return 'loss'
    if a == 'C' and b == 'G':
        return 'loss'
    if a == 'G' and b == 'P':
        return 'loss'
    else:
        return 'hikiwake'


if __name__ == '__main__':
    main()
