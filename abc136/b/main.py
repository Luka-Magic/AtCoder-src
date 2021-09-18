def main():
    c = 0
    n = int(input())
    for i in range(n):
        num = str(i + 1)
        if len(num) % 2 == 1:
            c += 1
    print(c)


if __name__ == '__main__':
    main()
