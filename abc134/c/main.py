import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')
from collections import Counter


def main():
    n = int(input())
    li = [int(input()) for _ in range(n)]
    li2 = li.copy()
    li2.sort()
    for i in li:
        if i != li2[-1]:
            print(li2[-1])
        else:
            print(li2[-2])

if __name__ == '__main__':
    main()
