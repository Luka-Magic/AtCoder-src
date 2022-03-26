import sys
input = sys.stdin.readline


def main():
    ans = float('inf')
    n = int(input())
    li = list(map(int, input().split()))
    for i in range(1, 101):
        k = 0
        for j in li:
            k += (i - j) ** 2
        ans = min(ans, k)
    print(ans)


if __name__ == '__main__':
    main()
