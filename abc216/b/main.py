import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [input().split() for _ in range(n)]
    for i in range(n):
        s, t = li[i]
        if i != n-1:
            for j in range(i+1, n):
                s_, t_ = li[j]
                if s == s_ and t == t_:
                    print('Yes')
                    exit()
    print('No')


if __name__ == '__main__':
    main()
