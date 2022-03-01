import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    masu = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n-5):
            c = 0
            for k in range(6):
                if masu[i][j+k] == '#':
                    c += 1
            if c >= 4:
                print('Yes')
                exit()

    for i in range(n-5):
        for j in range(n):
            c = 0
            for k in range(6):
                if masu[i+k][j] == '#':
                    c += 1
            if c >= 4:
                print('Yes')
                exit()

    for i in range(n-5):
        for j in range(n-5):
            c = 0
            for t in range(6):
                if masu[i+t][j+t] == '#':
                    c += 1
            if c >= 4:
                print('Yes')
                exit()

    for i in range(n-5):
        for j in range(5, n):
            c = 0
            for t in range(6):
                if masu[i+t][j-t] == '#':
                    c += 1
            if c >= 4:
                print('Yes')
                exit()
    print('No')


if __name__ == '__main__':
    main()
