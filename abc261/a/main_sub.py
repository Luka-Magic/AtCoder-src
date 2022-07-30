import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    l1, r1, l2, r2 = map(int, input().split())

    p1 = list(range(l1, r1))
    p2 = list(range(l2, r2))
    ans = 0
    for i in range(102):
        if i in p1 and i in p2:
            ans += 1
        
    print(ans)

if __name__ == '__main__':
    main()
