import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    k = int(input())
    a, b = map(int, input().split())
    for i in range(a, b+1):
        if i % k == 0:
            print('OK')
            exit()
    print('NG')


if __name__ == '__main__':
    main()
