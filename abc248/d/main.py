import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    q = int(input())
    dic = {}

    for i, v in enumerate(li):
        if v not in dic:
            dic[v] = [i+1]
        else:
            dic[v].append(i+1)
    import bisect
    for _ in range(q):
        l, r, x = map(int, input().split())
        if x not in dic:
            print(0)
        else:
            li_ = dic[x]
            l_idx = bisect.bisect_left(li_, l)
            r_idx = bisect.bisect_right(li_, r)
            print(r_idx - l_idx)

if __name__ == '__main__':
    main()
