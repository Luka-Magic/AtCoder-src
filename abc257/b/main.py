import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k, q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))
    for l in L: 
        if l == k:
            if A[l-1] != n:
                A[l-1] += 1
        else:
            if A[l-1] + 1 != A[l]:
                A[l-1] += 1
    print(*A)

if __name__ == '__main__':
    main()

acc new abc258
cd abc258

