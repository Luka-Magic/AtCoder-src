import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, q = map(int, input().split())
    li = list(range(1, n+1))
    indices = list(range(1, n+1))

    for _ in range(q):
        x = int(input())
        idx = indices[x-1]
        if idx == n:
            l_i, r_i = n-1, n
        else:
            l_i, r_i = idx, idx+1
        l, r = li[l_i-1], li[r_i-1]
        li[l_i-1], li[r_i-1] = li[r_i-1], li[l_i-1]
        indices[l-1], indices[r-1] = r_i, l_i
    print(*li)        
        

if __name__ == '__main__':
    main()
