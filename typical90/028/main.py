n = int(input())
li = [[0]*1002 for _ in range(1002)]
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    li[ly][lx] += 1
    li[ry][rx] += 1
    li[ry][lx] -= 1
    li[ly][rx] -= 1

for x in range(1002):
    for y in range(1, 1002):
        li[y][x] = li[y][x] + li[y-1][x]
for y in range(1002):
    for x in range(1, 1002):
        li[y][x] = li[y][x] + li[y][x-1]
ans = [0] * (n+1)

for y in range(1002):
    for x in range(1002):
        ans[li[y][x]] += 1

for i in ans[1:]:
    print(i)