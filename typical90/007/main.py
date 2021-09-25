from bisect import bisect_left
n = int(input())
li = list(map(int, input().split()))

q = int(input())

li.append(float('inf'))
li.append(-float('inf'))
li.sort()

for _ in range(q):
    b = int(input())
    i = bisect_left(li, b)
    print(min(b-li[i-1], li[i]-b))