import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    a, b = A[0], B[0]
    for i in range(1, n):
        a_n, b_n = -1, -1
        if a != -1:
            if abs(A[i] - a) <= k:
                a_n = A[i]
            else:
                a_n = -1
            if abs(B[i] - a) <= k:
                b_n = B[i]
            else:
                b_n = -1
        if b != -1:
            if abs(A[i] - b) <= k:
                a_n = A[i]
            elif a_n == -1:
                a_n = -1
            if abs(B[i] - b) <= k:
                b_n = B[i]
            elif b_n == -1:
                b_n = -1
        if a_n == -1 and b_n == -1:
            print('No')
            exit()
        a, b = a_n, b_n
    if a != -1 or b != -1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
