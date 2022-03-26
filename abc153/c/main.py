import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    li.sort()
    print(sum(li[:(n-k)]) if n >= k else 0)

if __name__ == '__main__':
    main()
