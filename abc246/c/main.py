import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k, x = map(int, input().split())
    li = list(map(int, input().split()))

    from collections import deque

    ans = sum(li)
    li_new = []
    li.sort(reverse=True)
    for i in range(n):
        a = li[i]
        if k == 0:
            print(ans)
            exit()
        if a > k*x:
            ans -= k*x
            print(ans)
            exit()
        else:
            li_new.append(a%x)
            k -= (a//x)
            ans = max(0, ans - (a - a%x))
    
    li_new.sort(reverse=True)
    for i in range(n):
        a = li_new[i]
        k -= 1
        if k == 0:
            print(max(0, ans - a))
            exit()
        ans = max(0, ans - a)
    print(max(ans, 0))    


if __name__ == '__main__':
    main()
