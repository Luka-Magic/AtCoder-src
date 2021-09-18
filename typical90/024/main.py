def main():
    n, k = map(int, input().split())
    a_l = list(map(int, input().split()))
    b_l = list(map(int, input().split()))
    p = 0
    for a, b in zip(a_l, b_l):
        p += abs(a - b)
    if p > k:
        print('No')
        exit()
    else:
        if (p - k) % 2 == 0:
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
