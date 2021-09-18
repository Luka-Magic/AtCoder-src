def main():
    n = int(input())
    li = list(map(int, input().split()))
    q = int(input())
    B = [int(input()) for _ in range(q)]

    li.sort()

    import bisect
    for b in B:
        le = bisect.bisect_left(li, b)
        if le == 0:
            print(abs(li[le] - b))
        elif le == n:
            print(abs(li[le-1] - b))
        else:
            print(min(abs(li[le-1]-b), abs(li[le]-b)))


if __name__ == '__main__':
    main()
