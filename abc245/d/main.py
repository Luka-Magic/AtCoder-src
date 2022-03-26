import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, m =map(int, input().split())
    A = list(map(int, input().split()))
    C = list(map(int, input().split()))
    B = [0] * (m+1)
    start = 0
    for a in A:
        if a != 0:
            break
        else:
            start += 1
    B[0] = C[start] // A[start]
    for i in range(1, m+1):
        B[i] = C[i+start] - sum([A[j+start] * B[i-j] for j in range(1, min(n+1-start, i+1))])
        B[i] //= A[start]
    print(*B)

if __name__ == '__main__':
    main()
