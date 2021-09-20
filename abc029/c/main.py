from itertools import product
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    li = ['a', 'b', 'c']

    for i in product(li, repeat=n):
        print(''.join(list(i)))


if __name__ == '__main__':
    main()
