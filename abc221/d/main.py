from collections import deque
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    p = [i[0] for i in li]
    p.sort()
    p = deque(p)
    q = [i[0] + i[1] for i in li]
    q.sort()
    q = deque(q)
    s, t = p.popleft(), q.popleft()
    l = [0] * (n + 1)
    now = 0
    log = 0
    while s != inf or t != inf:
        if s < t:
            l[log] += s - now
            log += 1
            now = s
            if p:
                s = p.popleft()
            else:
                s = inf
        elif s == t:
            # l[log] += 1
            # now = s
            if p:
                s = p.popleft()
            else:
                s = inf
            if q:
                t = q.popleft()
            else:
                t = inf
        else:
            l[log] += t - now
            log -= 1
            now = t
            if q:
                t = q.popleft()
            else:
                t = inf
    print(*l[1:])


if __name__ == '__main__':
    main()
