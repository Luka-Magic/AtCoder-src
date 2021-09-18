def main():
    a, b, c = map(int, input().split())

    k = c ** b - a
    if k > 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
