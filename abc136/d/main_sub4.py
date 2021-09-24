from itertools import groupby
s = input()

g = [[key, len(list(group))] for key, group in groupby(list(s))]
ans = [0] * len(s)
k = 0
for (_, rn), (_, ln) in zip(g[::2], g[1::2]):
    su = rn + ln
    ans[k + rn - 1] = (su + 1) // 2 if rn % 2 == 1 else su // 2
    ans[k + rn] = su // 2 if rn % 2 == 1 else (su + 1) // 2
    k += su
print(*ans)