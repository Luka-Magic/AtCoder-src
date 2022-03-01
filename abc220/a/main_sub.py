import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c = map(int, input().split())
    for i in range(a, b+1):
        if i % c == 0:
            print((i // c) * c)
            exit()
    print(-1)


if __name__ == '__main__':
    main()
