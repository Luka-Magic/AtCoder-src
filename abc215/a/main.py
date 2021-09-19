import sys
input = sys.stdin.readline


def main():
    s = 'Hello,World!'
    k = input().rstrip()
    if k == s:
        print('AC')
    else:
        print('WA')

if __name__ == '__main__':
    main()
