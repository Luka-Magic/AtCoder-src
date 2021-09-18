import collections
import sys
input = sys.stdin.readline


def main():
    n = int(input())
    li = list(map(int, input().split()))

    c = collections.Counter(li)
    cnt = 0
    for k, v in c.items():
        cnt += v*(v-1) // 2

    for l in li:
        print(cnt - (c[l]-1))


if __name__ == '__main__':
    main()
