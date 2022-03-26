import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    for i in li:
        if i % 2 != 0:continue
        if (i % 3 != 0) and (i % 5 != 0):
            print('DENIED')
            exit()
    print('APPROVED')



if __name__ == '__main__':
    main()
