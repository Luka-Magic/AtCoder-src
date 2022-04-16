import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    def f(i, n):
        if i == 1:
            return 1
        return str(f(i-1, n)) + ' ' + str(i) + ' ' + str(f(i-1, n))
    print(f(n, n))

if __name__ == '__main__':
    main()
