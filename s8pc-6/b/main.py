import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    A = []
    B = []
    ans = 0
    for _ in range(n):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        ans += b - a
    ad = inf
    for i in A:
        for j in B:
            k = 0
            for a in A:
                k += abs(a - i)
            for b in B:
                k += abs(b - j)
            ad = min(ad, k)
    print(ans + ad)
                    




if __name__ == '__main__':
    main()
