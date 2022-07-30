import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, c = map(int, input().split())
    
    def b2l(b):
        return list(map(int, list(bin(b)[2:].zfill(31))))
    
    for _ in range(n):
        t, a = map(int, input().split())
        if t == 1:
            



if __name__ == '__main__':
    main()
