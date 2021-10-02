import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    s = list(input())

    for i in s[1::2]:
        if i.islower():
            print('No')
            exit()
    for i in s[0::2]:
        if i.isupper():
            print('No')
            exit()
    print('Yes')


if __name__ == '__main__':
    main()
