import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b, c, d, e, f, x = map(int, input().split())
    aoki = 0
    takahashi = 0
    for i in range(x):
        if i % (a + c) < (a):
            aoki += b
        if i % (d + f) < (d):
            takahashi += e
    if aoki > takahashi:
        print('Takahashi')
    elif aoki < takahashi:
        print('Aoki')
    else:
        print('Draw')

if __name__ == '__main__':
    main()
