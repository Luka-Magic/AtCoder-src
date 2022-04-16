n = int(input())
li = [[0]*1002 for _ in range(1002)]
for _ in range(n):
    lx, ly, rx, ry = map(int, input().split())
    for y in range(ly, ry):
        li[y][lx] += 1
        li[y][rx] -= 1
li2 = [[0]*1002 for _ in range(1002)]
for y in range(1002):
    temp = 0
    for x in range(1002):
        temp += li[y][x]
        li2[y][x] = temp
ans = [0] * (n+1)
for y in range(1002):
    for x in range(1002):
        ans[li2[y][x]] += 1

for i in ans[1:]:
    print(i)