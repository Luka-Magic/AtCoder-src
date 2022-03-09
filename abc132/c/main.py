import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    print(li[n//2] - li[n//2-1])


if __name__ == '__main__':
    main()
