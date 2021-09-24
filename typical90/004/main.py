import numpy as np

h, w = map(int, input().split())
masu = np.array([list(map(int, input().split())) for _ in range(h)])

h_s = np.repeat(masu.sum(axis=1, keepdims=True), w, axis=1)
w_s = np.repeat(masu.sum(axis=0, keepdims=True), h, axis=0)

ans = h_s + w_s - masu
for l in ans:
    print(*l)
