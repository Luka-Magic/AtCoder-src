import sys
input = sys.stdin.readline


def main():
    n = int(input())
    while n >= 0:
        if n % 7 != 0:
            n -= 4
        else:
            print('Yes')
            break
    else:
        print('No')


if __name__ == '__main__':
    main()
