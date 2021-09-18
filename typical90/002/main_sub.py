from itertools import permutations


def main():
    n = int(input())
    if n % 2 == 1:
        print()
        exit()
    num = n // 2
    k = 0
    ans = []
    s = ['('] * num + [')'] * num
    c = permutations(s, n)
    c = set(c)
    for i, v in enumerate(c):
        k = 0
        for j in v:
            if j == '(':
                k += 1
            else:
                k -= 1
            if k < 0:
                break
        else:
            ans.append(''.join(v))

    ans.sort()
    for k in ans:
        print(k)


if __name__ == '__main__':
    main()
