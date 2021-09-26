from itertools import groupby
n = int(input())
S = input()

g = [len(list(group)) for key, group in groupby(list(S))]


def f(x):
    return x * (x+1) // 2


print(f(n) - sum([f(x) for x in g]))
