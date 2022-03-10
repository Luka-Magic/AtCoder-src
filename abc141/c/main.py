import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k, q = map(int, input().split())
    ans = [0] * n
    for _ in range(q):
        a = int(input())
        ans[a-1] += 1
    for i in ans:
        if i > q-k:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
