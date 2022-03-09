from re import I


mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    s = list(input())

    c = 0
    for i in range(n-1):
        if s[i] != s[i+1]:
            c += 1

    print(n - max(c - 2*k, 0) - 1)

if __name__ == '__main__':
    main()