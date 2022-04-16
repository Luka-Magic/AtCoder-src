import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    def f(a, b):
        return a**3 + a**2 * b + a * b**2 + b**3
    ans = float('inf')
    for a in range(10**6+1):
        low = -1
        high =10**6+1
        while low+1 < high:
            mid = (low + high) //2
            guess = f(a, mid)
            if guess >= n:
                high = mid
            else:
                low = mid
        ans = min(ans, f(a, high))
    print(ans)

if __name__ == '__main__':
    main()
