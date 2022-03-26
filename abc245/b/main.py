import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    li = list(map(int, input().split()))
    for i in range(2002):
        if i not in li:
            print(i)
            exit()


if __name__ == '__main__':
    main()
