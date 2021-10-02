# import sys
# input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    s = input()
    ans = ''
    for t, i in enumerate(s):
        if t == 0:
            ans += i.upper()
        else:
            ans += i.lower()
    print(ans)


if __name__ == '__main__':
    main()
