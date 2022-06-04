import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    S = input()
    can = ['A', 'T', 'C', 'G']
    ans = 0
    count = 0
    for s in S:
        if s in can:
            count += 1
            ans = max(count, ans)
        else:
            count = 0
    print(ans)


if __name__ == '__main__':
    main()
