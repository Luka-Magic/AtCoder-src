mod = 10**9 + 7
inf = float('inf')


def main():
    s = list(input())
    t = list(input())
    if s == t:
        print('Yes')
        exit()
    for i in range(len(s)-1):
        temp = s.copy()
        temp[i], temp[i+1] = temp[i+1], temp[i]
        if temp == t:
            print('Yes')
            exit()
    print('No')


if __name__ == '__main__':
    main()
