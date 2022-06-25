import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [[1]*(i+1) for i in range(n)]
    
    for i in range(n):
        for j in range(1, i):
            li[i][j] = li[i-1][j-1] + li[i-1][j]
        print(*li[i])


if __name__ == '__main__':
    main()
