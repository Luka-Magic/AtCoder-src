def main():
    n = int(input())
    x = input().split()
    dic = {'b': 1, 'c': 1, 'd': 2, 'w': 2, 't': 3, 'j': 3, 'f': 4, 'q': 4, 'l': 5, 'v': 5,
           's': 6, 'x': 6, 'p': 7, 'm': 7, 'h': 8, 'k': 8, 'n': 9, 'g': 9, 'z': 0, 'r': 0}
    ans = ''
    for s in x:
        temp = ''
        for i in s:
            i = i.lower()
            if i not in dic.keys():
                continue
            else:
                temp += str(dic[i])
        if temp:
            ans += temp
            ans += ' '
        else:
            continue
    if ans:
        if ans[-1] == ' ':
            ans = ans[:-1]
    print(ans)


if __name__ == '__main__':
    main()
