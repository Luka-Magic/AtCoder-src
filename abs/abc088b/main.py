def main():
    n = int(input())
    li = list(map(int, input().split()))

    li.sort(reverse=True)

    al = sum([i for i in li[::2]])
    bo = sum([i for i in li[1::2]])

    print(al - bo)


if __name__ == '__main__':
    main()
