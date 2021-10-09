n = input()
l = len(n)

ans = 0


def f(s, t, k):
    global ans
    if k == l:
        if s == '' or t == '':
            return
        s = sorted(s, reverse=True)
        t = sorted(t, reverse=True)
        ans = max(ans, int(''.join(s)) * int(''.join(t)))
        return
    else:
        return f(s + n[k], t, k+1), f(s, t + n[k], k+1)


f('', '', 0)
print(ans)
