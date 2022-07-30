from collections import deque
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, q = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n-1)]
    query = [list(map(int, input().split())) for _ in range(q)]

    ki = [[] for _ in range(n)]
    for a, b in li:
        ki[a-1].append(b-1)
        ki[b-1].append(a-1)

    dic = {}
    for p in query:
        if p[0]-1 not in dic:
            dic[p[0]-1] = p[1]
        else:
            dic[p[0]-1] += p[1]

    def bfs():
        ans = [0] * n
        seen = [0] * n
        que = deque([0])
        if 0 in dic:
            ans[0] = dic[0]
        while que:
            i = que.popleft()
            seen[i] = 1
            for j in ki[i]:
                if seen[j] != 0:
                    continue
                if j in dic:
                    ans[j] = ans[i] + dic[j]
                else:
                    ans[j] = ans[i]
                que.append(j)
        return ans
    
    ans = bfs()
    print(*ans)


if __name__ == '__main__':
    main()
