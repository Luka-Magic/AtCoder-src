import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if A[i] > B[i]:
            ans += B[i]
            continue
        else:
            ans += A[i]
            nokori = B[i] - A[i]
            if A[i+1] < nokori:
                ans += A[i+1]
                A[i+1] = 0
            else:
                ans += nokori
                A[i+1] -= nokori
    print(ans)


if __name__ == '__main__':
    main()
