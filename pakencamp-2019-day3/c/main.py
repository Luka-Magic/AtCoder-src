import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]
    from itertools import combinations
    ans = 0
    for t1, t2 in combinations(list(range(m)), 2):
        count = 0
        for i in range(n):
            count += max(li[i][t1], li[i][t2])
        ans = max(count, ans)
    print(ans)



if __name__ == '__main__':
    main()