import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    h, n = map(int, input().split())
    li = list(map(int, input().split()))
    print('Yes' if h <= sum(li) else 'No')


if __name__ == '__main__':
    main()
