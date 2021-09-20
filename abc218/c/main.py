import numpy as np


def main():
    n = int(input())
    s = np.array([list(input()) for _ in range(n)])
    t = np.array([list(input()) for _ in range(n)])
    ls = [0, 0, 0, 0]
    lt = [0, 0, 0, 0]

    def cut(S):
        for k in range(4):
            p = 0
            for i in range(n):
                if '#' in S[i]:
                    break
                else:
                    p += 1
            ls[k] = p
            S = np.rot90(S,)
        for k in range(4):
            p = ls[k]
            S = S[p:]
            S = np.rot90(S)
        return S
    ns = cut(s)
    nt = cut(t)
    flag = False
    for i in range(4):
        if (np.rot90(ns, i).shape) != nt.shape:
            continue
        if (np.rot90(ns, i) == nt).all():
            flag = True
    if flag:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
