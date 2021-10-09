import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, x = map(int, input().split())
    li = list(map(int, input().split()))
    k = (bin(x)[2:]).zfill(n)
    print(sum([a * int(b) for a, b in zip(li, list(k)[::-1])]))


if __name__ == '__main__':
    main()

