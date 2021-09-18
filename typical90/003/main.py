import sys
input = sys.stdin.readline


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n-1)]

    g = [[] for _ in range(n)]

    for l in li:
        a, b = l[0]-1, l[1]-1
        g[a].append(b)
        g[b].append(a)


    def f(a):
        for i in range(n):
            if i == a:continue



if __name__ == '__main__':
    main()