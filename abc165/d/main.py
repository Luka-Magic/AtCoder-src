import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    a, b, c = map(int, input().split())
    x = min(b-1, c)
    print(a * x //  b - a * (x // b))

if __name__ == '__main__':
    main()
