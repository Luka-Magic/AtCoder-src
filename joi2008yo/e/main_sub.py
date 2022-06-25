import sys
input = sys.stdin.readline
import numpy as np
mod = 10**9 + 7
inf = float('inf')


def main():
    r, c = map(int, input().split())
    li = np.array([list(map(int, input().split())) for _ in range(r)])
    s = (r - li.sum(axis=0))
    ans = int(s.sum())
    for i in range(2**r):
        s_ = np.zeros((2, c))
        s_[0, :] = s
        for j in range(r):
            if (i >> j) & 1:
                s_[0, :] += li[j, :] + (li[j, :] - 1)
        s_[1, :] = r - s_[0, :]
        ans = max(int(ans), int(np.max(s_, axis=0).sum()))
    print(ans)


if __name__ == '__main__':
    main()
