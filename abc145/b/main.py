mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    s = input()
    if n % 2 == 1:
        print('No')
        exit()
    if s[:n//2] == s[n//2:]:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()

