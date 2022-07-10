from itertools import permutations
n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

for i, m in enumerate(permutations(list(range(n)), n)):
    for j, s in enumerate(m):
        if s + 1 != p[j]:
            break
    else:
        a = i
    for j, s in enumerate(m):
        if s + 1 != q[j]:
            break
    else:
        b = i
print(abs(a - b))
