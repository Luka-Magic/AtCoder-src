import bisect
import sys
input = sys.stdin.readline


def main():
    h, w, n = map(int, input().split())
    h_l, w_l = [], []
    for _ in range(n):
        a, b = map(int, input().split())
        h_l.append(a)
        w_l.append(b)

    # h_, w_ = np.argsort(h_l), np.argsort(w_l)

    def argsort(li):
        li_ = li.copy()
        li_ = list(set(li_))
        li_.sort()
        re = []
        for i in li:
            re.append(bisect.bisect_left(li_, i))
        return re

    h_, w_ = argsort(h_l), argsort(w_l)
    for i, j in zip(h_, w_):
        print(i+1, j+1)

if __name__ == '__main__':
    main()
