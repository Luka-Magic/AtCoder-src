import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, h = map(int, input().split())
    a, b, c, d, e = map(int, input().split())

    def f(x, y, z):
        return x * a + y * c
    def man(x, y, z):
        return h + (x * b + y * d - z * e)
    ans = inf
    for x in range(n+1):
        low = -1
        high = n - x
        while low + 1 < high:
            mid = (low + high) //2
            guess = man(x, mid, (n-mid-x))
            if guess > 0:
                high = mid
            else:
                low = mid
        ans = min(ans, f(x, high, n-high-x))
    print(ans)
    
if __name__ == '__main__':
    main()
