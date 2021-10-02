import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a = int(input())
    b = int(input())
    print(min((a-b) % 10, (b-a) % 10))


if __name__ == '__main__':
    main()
