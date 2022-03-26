import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    ans = 0
    mi = float('inf')
    n = int(input())
    li = list(map(int, input().split()))
    for l in li:
        if mi > l:
            mi = l
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
