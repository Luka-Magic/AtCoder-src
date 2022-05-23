import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

import heapq

def dijkstra(s, n, c_list):
    _list = [float("Inf")]*n
    _list[s] = 0
    hq = [[0,s]]
    heapq.heapify(hq)
    while len(hq) > 0:
        _ci, _i = heapq.heappop(hq)
        if _list[_i] < _ci:
            continue
        for _cj,_j in c_list[_i]:
            if _list[_j] > (_list[_i] + _cj):
                _list[_j] = _list[_i] + _cj
                heapq.heappush(hq, [_list[_j],_j])
    return _list

def main():
    n, m = map(int, input().split())
    g_list = [[] for i in range(n)]

    for _ in range(m):
        _a, _b, _c = map(int, input().split())
        g_list[_a-1].append([_c,_b-1])
    
    
    print(g_list)
    go = dijkstra(0, n, g_list)
    print(go)
    


if __name__ == '__main__':
    main()
