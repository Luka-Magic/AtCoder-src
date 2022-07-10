n = int(input())
s = set(map(int, input().split()))
q = int(input())
t = set(map(int, input().split()))

ans = 0

for i in t:
    if i in s:
        ans += 1

print(ans)
