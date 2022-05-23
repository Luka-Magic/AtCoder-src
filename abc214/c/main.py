import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))
    
    now = T[0]
    print(now)
    for i in range(1, n):
        now = min(now+S[i-1], T[i])
        print(now)

if __name__ == '__main__':
    main()