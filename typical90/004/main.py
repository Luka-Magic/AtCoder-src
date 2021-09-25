import numpy as np

h, w = map(int, input().split())
masu = np.array([list(map(int, input().split())) for _ in range(h)])

h_s = masu.sum(axis=1)
w_s = masu.sum(axis=0)

ans = h_s[:, None] + w_s[None, :] - masu
for l in ans:
    print(' '.join(map(str, l.tolist())))
