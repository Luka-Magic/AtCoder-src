import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans = [-1]*n
    a = []
    for i, l in enumerate(li[::-1]):
        k = n-i
        t = [(i+1)*k for i in range(n//k)]
        c = 0
        for p in t[::-1]:
            if p == k:
                break
            c += ans[p-1] % 2
        ans[k-1] = (l + c) % 2
        if (l + c) % 2 == 1:
            a.append(k)

    print(len(a))
    if len(a) == 0:
        exit()
    print(*a)


if __name__ == '__main__':
    main()
