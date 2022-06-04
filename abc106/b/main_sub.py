import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1, 2):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 8:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
