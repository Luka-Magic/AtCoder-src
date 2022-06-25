mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(1000):
        q = str(i).zfill(3)
        c = 0
        for num in s:
            if num == q[c]:
                c += 1
            if c == 3:
                ans += 1
                break
    print(ans)





if __name__ == '__main__':
    main()
