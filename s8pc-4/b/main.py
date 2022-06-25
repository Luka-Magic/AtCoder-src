import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = inf
    for i in range(2**n):
        c = 0
        k_ = 1
        max_ = 0
        for j in range(1, n):
            if (i >> j) & 1:
                c += A[j-1] - A[j] + 1
                A[j] = A[j-1] + 1
        for j in range(1, n):
            if A[j] > A[j-1]:
                k_ += 1
        if k_ >= k:
            ans = min(ans, c)
    print(ans)

                




if __name__ == '__main__':
    main()
