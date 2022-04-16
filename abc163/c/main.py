import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    from collections import Counter
    c = Counter(li)
    for i in range(1, n+1):
        if i in c:
            print(c[i])
        else:
            print(0)

if __name__ == '__main__':
    main()
