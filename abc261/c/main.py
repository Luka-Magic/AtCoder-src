mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    S = dict()
    for i in range(n):
        s = input()
        if s not in S:
            S[s] = 0
            print(s)
        else:
            num = S[s]
            num += 1
            print(f'{s}({num})')
            S[s] += 1


if __name__ == '__main__':
    main()
