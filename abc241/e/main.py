import bisect
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))

    t = 0
    A = []
    se = set()
    ans = 0

    while 1:
        i = ans % n
        if t == k:
            print(ans)
            exit()
        if i in se:
            break
        t += 1
        se.add(i)
        A.append(i)
        ans += li[i]

    cycle_i = A.index(i)
    cycle = A[cycle_i:]
    c_s = sum([li[i] for i in cycle])
    init = t - len(cycle)

    cycle_n = (k - init) // len(cycle)
    cycle_p = (k - init) % len(cycle)

    ans += (cycle_n - 1) * c_s
    ans += sum([li[i] for i in cycle[:cycle_p]])
    print(ans)


if __name__ == '__main__':
    main()
