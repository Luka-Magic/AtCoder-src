import sys
input = sys.stdin.readline


def main():
    n = int(input())
    ans = 0
    while 1:
        if 2**ans <= n:
            ans += 1
        else:
            break
    print(ans-1)


if __name__ == '__main__':
    main()
