import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    k_li = []
    li = []
    for _ in range(m):
        k, *l = map(int, input().split())
        k_li.append(k)
        li.append(l)
    P = list(map(int, input().split()))
    ans = 0
    for i in range(2**n):
        c = [0] * m
        for j in range(n):
            if (i >> j) & 1:
                for k in range(m):
                    if j+1 in li[k]:
                        c[k] += 1
        for a, b in enumerate(c):
            if b % 2 != P[a]:
                break
        else:
            ans += 1
    print(ans)







if __name__ == '__main__':
    main()
