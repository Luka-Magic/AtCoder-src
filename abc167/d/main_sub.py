import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    li = list(map(lambda x:int(x)-1, input().split()))
    now = 0
    c = 0
    s = set([0])
    l = [0]
    while 1:
        now = li[now]
        c += 1
        if c == k:
            print(now + 1)
            exit()
        if now in s:
            break
        else:
            s.add(now)
            l.append(now)
    
    idx = l.index(now)
    cycle = l[idx:]
    cy_num = len(cycle)
    ans = k - idx

    print(cycle[ans%cy_num] + 1)
    exit()


if __name__ == '__main__':
    main()
