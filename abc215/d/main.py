def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])
    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    arr = list(map(lambda x: x[0], arr))

    return arr


n, m = map(int, input().split())
li = list(map(int, input().split()))
no = set()

for i in li:
    arr = factorization(i)
    for s in arr:
        no.add(s)

hante = [1] * (m+1)
for s in no:
    if s == 1:
        continue
    for i in range(0, m+1, s):
        hante[i] = 0
print(sum(hante))
for a in range(1, m+1):
    if hante[a] == 1:
        print(a)
