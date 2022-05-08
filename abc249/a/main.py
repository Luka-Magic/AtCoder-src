from re import S


a, b, c, d, e, f, x = map(int, input().split())

def leng(a, b, c):
    s = x // (a + c)
    t = x % (a + c)
    return s * a * b + min(t, a) * b
if leng(a, b, c) > leng(d, e, f):
    print('Takahashi')
elif leng(a, b, c) < leng(d, e, f):
    print('Aoki')
else:
    print('Draw')