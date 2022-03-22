import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c1 = 0
    for i in range(n):
        if a[i] == b[i]:
            c1 += 1
    print(c1)
    a = set(a)
    b = set(b)
    print(len(a & b) - c1)


if __name__ == '__main__':
    main()
