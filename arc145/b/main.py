n, a, b = map(int, input().split())

if a <= b:
    print(max(n - a + 1, 0))
else:
    no = n - a + 1
    k = no // a
    q = no % a
    q = min(q, b)
    ans = k * b + q
    print(max(ans, 0))