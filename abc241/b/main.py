import sys

input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    from collections import Counter

    c = Counter(A)
    for b in B:
        if c[b] > 0:
            c[b] -= 1
        else:
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    main()
