import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    m = 2025
    n = int(input())
    k = m - n
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == k:
                print(str(i) + ' x ' + str(j))


if __name__ == '__main__':
    main()
