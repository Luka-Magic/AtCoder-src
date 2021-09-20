import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    i = 0
    while 1:
        if k ** i > n:
            print(i)
            exit()
        else:
            i += 1


if __name__ == '__main__':
    main()
