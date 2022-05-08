mod = 10**9 + 7
inf = float('inf')


def main():
    s = input()
    l = []
    for i in s:
        l.append(int(i))
    for i in range(10):
        if i not in l:
            print(i)
            exit()


if __name__ == '__main__':
    main()
