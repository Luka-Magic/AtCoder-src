import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort(reverse=True)
    su = li[0]
    for i in range(n-2):
        su += li[i // 2 + 1]
    print(su)
    

if __name__ == '__main__':
    main()