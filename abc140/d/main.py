from re import I


mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    s = list(input())
    from itertools import groupby
    g = [[key, len(list(group))] for key, group in groupby(s)]
    print(n - max(len(g) - 1 - 2*k, 0) - 1)

if __name__ == '__main__':
    main()