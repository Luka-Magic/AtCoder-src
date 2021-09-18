def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    q = int(input())
    li_q = [list(map(int, input().split())) for _ in range(q)]

    li1_s = [0]
    li2_s = [0]
    for i in range(n):
        if li[i][0] == 1:
            li1_s.append(li1_s[-1] + li[i][1])
            li2_s.append(li2_s[-1])
        else:
            li2_s.append(li2_s[-1] + li[i][1])
            li1_s.append(li1_s[-1])

    import bisect
    for i in range(q):
        a, b = li_q[i][0], li_q[i][1]
        print(li1_s[b] - li1_s[a-1], li2_s[b] - li2_s[a-1])


if __name__ == '__main__':
    main()
