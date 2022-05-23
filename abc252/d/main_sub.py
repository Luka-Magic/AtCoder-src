import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    ans = 0
    from collections import Counter
    c = [v for v in Counter(li).values()]
    ans = sum(c) ** 3
    for i in c:
        ans -= i**3
    
    c2 = [v**2 for v in c]
    k2 = sum(c) * sum(c2)
    for i in c:
        k2 -= i**3
    print((ans - 3 * k2) // 6)
    
    



if __name__ == '__main__':
    main()
