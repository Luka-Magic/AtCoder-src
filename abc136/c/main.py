def main():
    n = int(input())
    li = list(map(int, input().split()))

    now = li[0]-1
    for l in li[1:]:
        if l < now:
            print('No')
            break
        if now < l:
            now = l-1
    else:
        print('Yes')


if __name__ == '__main__':
    main()
