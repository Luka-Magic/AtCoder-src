import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())

    ans = ''
    k = 1
    if n == 1:
        print('A')
        exit()

    while n != 0:
        if n % 2 == 0:
            ans += 'B'
            n //= 2
        else:
            ans += 'A'
            n -= 1

    print(ans[::-1])


if __name__ == '__main__':
    main()
