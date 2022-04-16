mod = 10**9 + 7
inf = float('inf')

def main():
    s = input()
    t = input()
    print('Yes' if s == t[:-1] else 'No')


if __name__ == '__main__':
    main()
