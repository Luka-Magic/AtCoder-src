import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    k = n // 4
    p = n % 4
    print(n * 2)
    print(int(str(p) + str(4) * k))

if __name__ == '__main__':
    main()
