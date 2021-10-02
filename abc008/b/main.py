import sys
from collections import Counter
# input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [input() for _ in range(n)]
    c = Counter(li)
    print(c.most_common(1)[0][0])


if __name__ == '__main__':
    main()
