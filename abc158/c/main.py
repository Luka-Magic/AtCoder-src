import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    a, b = map(int, input().split())
    for i in range(1, 10**6):
        if int(i * 0.08) == a and int(i * 0.10) == b:
            print(i)
            exit()
    print(-1)

if __name__ == '__main__':
    main()

