from itertools import permutations
import sys
input = sys.stdin.readline


def main():
    s, k = input().split()
    k = int(k)
    s = list(s)
    l = len(s)
    li = []
    for i in permutations(s, l):
        i = ''.join(i)
        li.append(i)
    li = set(li)
    li = list(li)
    li.sort()
    print(li[k-1])


if __name__ == '__main__':
    main()
