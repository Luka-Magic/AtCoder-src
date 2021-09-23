n = int(input())
ans = []


def f(s, i):
    if i >= n:
        ans.append(s)
        return None
    else:
        return f(s+'a', i+1), f(s+'b', i+1), f(s+'c', i+1)

f('', 0)

ans.sort()
print(*ans, sep='\n')