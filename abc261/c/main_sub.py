mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    dic = dict()
    S = set()
    for i in range(n):
        s = input()
        if s not in S:
            S.add(s)
            dic[s] = 0
            print(s)
        else:
            num = dic[s]
            num += 1
            print(f'{s}({num})')
            dic[s] += 1


if __name__ == '__main__':
    main()
