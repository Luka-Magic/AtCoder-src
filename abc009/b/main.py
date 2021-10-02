import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]
    li = list(set(li))
    li.sort()
    print(li[-2])


if __name__ == '__main__':
    main()
