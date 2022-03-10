import math
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b = map(int, input().split())

    ans = set()
    ceil = int(max(math.sqrt(a), math.sqrt(b)))
    for i in range(1, ceil):
        if a % i == 0 and b % i == 0 and i <= min(a, b):
            ans.add(i)
            p = a//i
            q = b//i
            if a % p == 0 and b % p == 0 and p <= min(a, b):
                ans.add(p)
            if a % q == 0 and b % q == 0 and q <= min(a, b):
                ans.add(q)
    ans2 = set()
    li = list(ans)
    for i in li:
        if i not in ans:
            continue
        if i == 1:
            continue
        delset = set()
        for j in ans:
            if j == i:
                continue
            if j % i == 0:
                delset.add(j)
        ans = ans - delset

    print(len(ans))


if __name__ == '__main__':
    main()
