import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    li = list(map(lambda x: -1 * int(x), input().split()))

    import heapq
    heapq.heapify(li)
    for _ in range(m):
        a = heapq.heappop(li)
        b = int(a/2)
        heapq.heappush(li, b)
    ans = 0
    while li:
        ans += heapq.heappop(li)
    print(ans * -1)

if __name__ == '__main__':
    main()
