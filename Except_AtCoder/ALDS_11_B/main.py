n = int(input())
li = [sorted(list(map(lambda x:int(x) - 1, input().split()))[2:])
      for _ in range(n)]

seen = [0] * n
done = [0] * n
t = 0


def dfs(i):
    global t
    t += 1

    seen[i] = t
    for j in li[i]:
        if seen[j] == 0:
            dfs(j)
    t += 1
    done[i] = t

for i in range(n):
    if seen[i] != 0:continue
    dfs(i)

for i, j, k in zip(range(n), seen, done):
    print(i+1, j, k)
