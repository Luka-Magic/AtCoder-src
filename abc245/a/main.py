import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c, d = map(int, input().split())
    if a*3600 + b * 60 < c * 3600 + d * 60 + 1:
        print('Takahashi')
    else:
        print('Aoki')

if __name__ == '__main__':
    main()
