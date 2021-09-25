from collections import deque
import sys
sys.setrecursionlimit(1000000)  # 再帰関数の上限


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n-1)]

    g = [[] for _ in range(n)]
    for a, b in li:
        g[a-1].append(b-1)
        g[b-1].append(a-1)

    def bfs(i):
        seen = [0] * n
        que = deque([i])
        seen[i] = -1
        while que:
            key = que.popleft()
            for i in g[key]:
                if seen[i]:
                    continue
                seen[i] = seen[key] * -1
                que.append(i)
        return seen

    seen = bfs(0)
    if sum(seen) > 0:
        flag = 1
    else:
        flag = -1

    ans = []
    for i in range(n):
        if seen[i] == flag:
            ans.append(i+1)
    print(*ans[:n//2])


if __name__ == '__main__':
    main()
