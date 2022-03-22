a, b = map(str, input().split())
A = a * int(b)
B = b * int(a)
li = [A, B]
li.sort()
print(li[0])