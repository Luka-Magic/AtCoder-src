import bisect

mod = 10**9 + 7
inf = float('inf')
 

q = int(input())
A = []
for _ in range(q):
    k = list(map(int, input().split()))
    if k[0] == 1:
        bisect.insort(A, k[1])
    elif k[0] == 2:
        i = bisect.bisect(A, k[1])
        if len(A[:i]) < k[2]:
            print(-1)
            continue
        else:
            print(A[i-k[2]])
    elif k[0] == 3:
        i = bisect.bisect_left(A, k[1])
        if len(A[i:]) < k[2]:
            print(-1)
            continue
        else:
            print(A[i+k[2]-1])