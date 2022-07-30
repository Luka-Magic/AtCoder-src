from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, a, b = map(int, input().split())
    li = list(map(int, input().split()))

    low = 0
    high = 10**10
    li.sort()

    while low + 1 < high:
        mid = (low + high) // 2
        thre = bisect_right(li, mid)
        
        f_d = sum([(mid + a - 1 - v) // a for v in li[:thre]])
        s_d = sum([(v - mid) // b for v in li[thre:]])
        
        if f_d > s_d:
            high = mid
        else:
            low = mid
        
    print(low)


if __name__ == '__main__':
    main()
