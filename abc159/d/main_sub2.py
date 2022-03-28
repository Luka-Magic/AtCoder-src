import collections
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    li = list(map(int, input().split()))

    c = collections.Counter(li)

    k = sum([i*(i-1)//2 for i in c.values()])

    for i in li:
        print(k - (c[i]-1))


if __name__ == '__main__':
    main()
