import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    r = 0
    for i in range(n):
        l = min(B[i], A[i]-r)
        r = min(B[i]-l, A[i+1])
        ans += l + r
    print(ans)

    


if __name__ == '__main__':
    main()
