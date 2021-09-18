import heapq


def main():
    n, k = map(int, input().split())
    li_ = [list(map(int, input().split())) for _ in range(n)]
    li = list(map(lambda x: [x[1]*(-1), (x[0]-x[1])*(-1)], li_))
    heapq.heapify(li)

    ans = 0
    for _ in range(k):
        m = heapq.heappop(li)
        ans += m[0] * (-1)
        heapq.heappush(li, [m[1], 0])
    print(ans)


if __name__ == '__main__':
    main()
