import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    li = list(map(lambda x:int(x)-1, input().split()))
    now = 0
    c = 0
    l = [0]
    s = set()
    while 1:
        now = li[now]
        c += 1
        if c == k:
            print(now + 1)
            exit()
        if now in s:
            break
        else:
            l.append(now)
            s.add(now)
    init = l.index(now)
    cycle = l[init:]
    print(cycle[(k-init)%len(cycle)]+1)


if __name__ == '__main__':
    main()
