import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [1]
    if n == 1:
        print(1)
        exit()

    for i in range(2, n+2):
        l = []
        for j in range(i-1):
            if 0 < j < i-2:
                l.append(li[j] + li[j-1])
            else:
                l.append(1)
        print(*l)
        li = l.copy()


        



if __name__ == '__main__':
    main()
