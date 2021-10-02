import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans = 0
    for i in li:
        for j in range(10):
            if ((i - j) % 3 == 2) or ((i - j) % 2 == 0):
                continue
            else:
                ans += j
                # print(i, j)
                break
    print(ans)


if __name__ == '__main__':
    main()
