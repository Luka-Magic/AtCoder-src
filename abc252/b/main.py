import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    ma = max(A)
    for b in B:
        if A[b-1] == ma:
            print('Yes')
            exit()
    print('No')

if __name__ == '__main__':
    main()
