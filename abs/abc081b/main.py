def main():
    n = int(input())
    li = list(map(int, input().split()))
    ans_li = []
    for k in li:
        t = 0
        a = k
        while 1:
            if a % 2 == 1:
                break
            else:
                t += 1
                a = a//2
        ans_li.append(t)
    print(min(ans_li))


if __name__ == '__main__':
    main()
