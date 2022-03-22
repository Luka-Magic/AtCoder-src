import sys
input = sys.stdin.readline

from itertools import combinations

def main():
    n = int(input())
    s = set()
    ans = 0
    for _ in range(n):
        x, y = map(int, input().split())
        s.add((x, y))
    li = list(s)
    for i, j in combinations(list(range(n)), 2):
        x1, y1 = li[i]
        x2, y2 = li[j]
        if (x1 == x2) or (y1 == y2):
            continue
        if ((x1, y2) in s) and ((x2, y1) in s):
            ans += 1
    print(ans // 2)

if __name__ == '__main__':
    main()
