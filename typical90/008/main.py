def main():
    n = int(input())
    S = input()

    mod = 10**9 + 7

    dic = {}
    for s in 'atcoder':
        dic[s] = [i for i in range(n) if S[i] == s]

    for i, s in enumerate(S[::-1]):
        dic[s]

    


if __name__ == '__main__':
    main()
