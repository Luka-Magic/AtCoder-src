import sys
input = sys.stdin.readline


def main():
    n, m, t = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(m)]
    l = [0]
    for a, b in li:
        l.append(a)
        l.append(b)
    l.append(t)
    flag = True
    bat = n
    now = 0
    for i in l:
        if flag == False:
            bat -= (i - now)
            if bat <= 0:
                print('No')
                exit()
        elif flag == True:
            bat += (i - now) * 1
            bat = min(bat, n)
        # 更新
        if flag:
            flag = False
        else:
            flag = True
        now = i
    print('Yes')


if __name__ == '__main__':
    main()
