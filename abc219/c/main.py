def main():
    x = ['0'] + list(input())
    n = int(input())
    people = [input() for _ in range(n)]
    ml = 0
    for p in people:
        ml = max(ml, len(p))

    ans = people
    for t in range(ml-1, -1, -1):
        temp = []
        for p in ans:
            if t >= len(p):
                i = '0'
            else:
                i = p[t]
            for k, al in enumerate(x):
                if i == al:
                    temp += [[p, k]]
        temp.sort(key=lambda x: x[1])
        ans = list(map(lambda x: x[0], temp))

    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
