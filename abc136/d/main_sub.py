def main():
    s = input()

    lr = [0]
    for i in range(len(s) - 1):
        if s[i] == 'L' and s[i+1] == 'R':
            lr.append(i+1)
    lr.append(len(s))

    ans = []

    for i in range(len(lr)-1):
        RL = s[lr[i]:lr[i+1]]
        le = len(RL)
        if not RL:
            continue
        for j, k in enumerate(RL):
            if j == '0' and k == 'L':
                ans += [le] + [0] * (le - 1)
                break
            elif k == 'L':
                if le % 2 == 0:
                    ans += [0] * (j-1) + [le//2] * 2 + [0] * (le-j-1)
                    break
                else:
                    if j % 2 == 1:
                        l = le//2 + 1
                        r = le//2
                    elif j % 2 == 0:
                        l = le//2
                        r = le//2 + 1
                    ans += [0] * (j-1) + [l] + [r] + [0] * (le-j-1)
                    break
            elif j == le-1 and k == 'R':
                ans += [0] * (le-1) + [le]
                break
    print(' '.join(list(map(str, ans))))


if __name__ == '__main__':
    main()
