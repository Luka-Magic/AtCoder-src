from itertools import permutations


def main():
    n = int(input())
    if n % 2 == 1:
        print()
        exit()
    ans = []
    for i in range(2**n):
        k = bin(i)[2:].zfill(n).replace('0', '(').replace('1', ')')
        if k.count('(') != n//2:
            continue
        c = 0
        for j in list(k):
            if j == '(':
                c += 1
            else:
                c -= 1
            if c < 0:
                break
        else:
            ans.append(k)

    ans.sort()
    for t in ans:
        print(t)


if __name__ == '__main__':
    main()