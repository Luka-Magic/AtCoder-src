def main():
    n = int(input())
    li = list(map(int, input().split()))

    now = li[0]

    for i in li[1:]:
        if i > now:
            now = i
        if i + 1 < now:
            print('No')
            exit()
    else:
        print('Yes')

if __name__ == '__main__':
    main()
