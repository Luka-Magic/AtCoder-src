import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = 0
    bef = -100
    for i in range(n):
        r = a[i] - 1
        ans += b[r]
        if i == 0:
            bef = r
        else:
            if r - bef == 1:
                ans += c[bef]
            bef = r
    print(ans)




if __name__ == '__main__':
    main()
