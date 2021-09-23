s, k = input().split()
k = int(k) - 1
ans = set()


def f(now, last):
    if not last:
        ans.add(now)
        return
    else:
        for i in range(len(last)):
            new_now = now + last[i]
            new_last = last[:i] + last[i+1:]
            f(new_now, new_last)


f('', s)
ans = sorted(ans)
print(ans[k])