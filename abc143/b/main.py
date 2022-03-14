import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            ans += li[i] * li[j]
    print(ans)



if __name__ == '__main__':
    main()
