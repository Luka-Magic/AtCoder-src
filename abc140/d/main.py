mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    s = list(input())
    from itertools import groupby
    rl = [[key,len(list(group))] for key,group in groupby(s)]
    print(n-max(1, len(rl)-2*k))

if __name__ == '__main__':
    main()