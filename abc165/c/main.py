import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

from itertools import combinations_with_replacement


def main():
    n, m, q = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(q)]
    ans = 0
    for i in combinations_with_replacement(list(range(m)), n):
        temp = 0
        for a, b, c, d in li:
            if i[b-1] - i[a-1] == c:
                temp += d
        ans = max(ans, temp)
    print(ans)

if __name__ == '__main__':
    main()
