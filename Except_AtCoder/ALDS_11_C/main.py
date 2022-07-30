from collections import deque
n = int(input())
li = [list(map(lambda x:int(x)-1, input().split()))[2:] for _ in range(n)]

seen = [-1] * n
seen[0] = 0

que = deque([0])
while que:
    a = que.popleft()
    for b in li[a]:
        if seen[b] != -1:
            continue
        seen[b] = seen[a]+1
        que.append((b))

for i in range(n):
    print(i+1, seen[i])
