n = int(input())

ans = 0
while 2**(ans + 1) <= n:
    ans += 1
print(ans)
