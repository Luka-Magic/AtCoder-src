import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    ans = set()
    no = dict()
    se = 0
    pe = 0
    for _ in range(m):
        p, s = map(str, input().split())
        if p in ans:
            continue
        else:
            if s == 'AC':
                if p in no:
                    pe += no[p]
                ans.add(p)
                se += 1
            else:
                if p not in no:
                    no[p] = 1
                else:
                    no[p] += 1
    print(se, pe)

if __name__ == '__main__':
    main()
