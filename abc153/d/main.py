import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    h = int(input())
    ans = 0
    p = 1
    while h:
        if h > 1:
            h = h//2
            ans += p
            p *= 2
        else:
            h = 0
            ans += p
    print(ans)

if __name__ == '__main__':
    main()