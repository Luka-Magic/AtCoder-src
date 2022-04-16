import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    a, b = list(input().split())
    b = int(b[:-3] + b[-2:])
    print((int(a) * b)//100)

if __name__ == '__main__':
    main()
