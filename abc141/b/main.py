mod = 10**9 + 7
inf = float('inf')


def main():
    s = input()
    for i, d in enumerate(list(s)):
        if i%2 == 0:
            if d == 'L':
                print('No')
                exit()
        if i%2 == 1:
            if d == 'R':
                print('No')
                exit()
    print('Yes')

if __name__ == '__main__':
    main()
