mod = 10**9 + 7
inf = float('inf')


def main():
    s = input()
    se = set()
    for i in s:
        se.add(i)
    if len(list(s)) != len(se):
        print('No')
        exit()
    if s.lower() == s:
        print('No')
        exit()
    if s.upper() == s:
        print('No')
        exit()
    print('Yes')




if __name__ == '__main__':
    main()
