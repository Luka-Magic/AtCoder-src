mod = 10**9 + 7
inf = float('inf')


def main():
    n, a, b = map(int, input().split())
    for i in range(n * a):
        flag = False
        if (i // a) % 2 != 0:
            flag = ~flag
        for j in range(n * b):
            if (j // b) % 2 != 0:
                f = ~flag
            else:
                f = flag
            if f:
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    main()
