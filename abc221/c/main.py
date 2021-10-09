from itertools import permutations
import math

mod = 10**9 + 7
inf = float('inf')


def main():
    n = list(input())
    l = len(n) // 2 + 1
    ans = 0
    for i in permutations(n, len(n)):
        for j in range(1, l):
            s = i[:j]
            t = i[j:]
            if s[0] == '0' or t[0] == '0':
                continue
            s = int(''.join(s))
            t = int(''.join(t))
            ans = max(s * t, ans)
    print(ans)


if __name__ == '__main__':
    main()
