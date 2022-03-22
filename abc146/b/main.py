mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    s = list(input())

    def f(i):
        return chr((ord(i)-65+n) % 26 + 65)
    ans = list(map(f, s))
    print(''.join(ans))


if __name__ == '__main__':
    main()
