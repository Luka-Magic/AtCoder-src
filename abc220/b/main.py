import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    k = int(input())
    a, b = input().split()
    print(int(a, k) * int(b, k))


if __name__ == '__main__':
    main()
