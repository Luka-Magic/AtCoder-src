mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [input() for _ in range(n)]
    li.sort()
    from itertools import groupby
    rl = [[key,len(list(group))] for key,group in groupby(li)]
    m = max(rl, key = lambda x:x[1])[1]
    for i, v in rl:
        if v == m:
            print(i)


if __name__ == '__main__':
    main()
