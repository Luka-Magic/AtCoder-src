n = int(input())
li = ['a', 'b', 'c']


def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n)+str(X % n)
    return str(X % n)


for i in range(3**n):
    s = Base_10_to_n(i, 3).zfill(n)
    ans = ''.join([li[int(i)] for i in s])
    print(ans)
