mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    s = list(input())
    from itertools import groupby
    s = [[key, len(list(group))] for key, group in groupby(s)]
    print(len(s))


if __name__ == '__main__':
    main()
