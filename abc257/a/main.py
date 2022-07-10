import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, x = map(int, input().split())
    li = []
    for i in range(26):
        li.extend([chr(i+97)] * n)
    print(li[x-1].upper())


if __name__ == '__main__':
    main()