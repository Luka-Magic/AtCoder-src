import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li2 = list(range(1, n+1))
    c = 0
    for p, q in zip(li, li2):
        if p != q:
            c += 1
    if c == 0 or c == 2:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
