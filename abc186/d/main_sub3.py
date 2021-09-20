n = int(input())
li = list(map(int, input().split()))
li.sort()
cli = [li[0]]
for i in li[1:]:
    cli.append(cli[-1] + i)
ans = 0
for i in range(1, n):
    ans += li[i] * i - cli[i-1]
print(ans)
