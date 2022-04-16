import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, l = map(int, input().split())
    li = [list(input()) for _ in range(n)]
    s = [set() for _ in range(n)]
    for i, l in enumerate(li):
        for a in l:
            s[i].add(a)
    k = 0
    for i in range(n):
        for j in range(i+1, n):
            k += len(s[i]) + len(s[j]) - len(s[i] & s[j])
    


if __name__ == '__main__':
    main()
