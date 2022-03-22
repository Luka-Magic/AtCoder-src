import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    s = input()
    ans = 0
    for i in range(2, n):
        if s[i-2:i+1] == 'ABC':
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
