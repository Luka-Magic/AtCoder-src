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
    b = [v for v in Counter(li).values()]
    a = [0]
    for i in b[:-1]:
        a.append(a[-1] + i)
    c = [0]
    for i in b[1:][::-1]:
        c.append(c[-1] + i)
    c = c[::-1]
    ans = 0
    for i, j, k in zip(a, b, c):
        ans += i*j*k
    print(ans)    
    



if __name__ == '__main__':
    main()
