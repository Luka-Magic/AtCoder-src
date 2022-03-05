from collections import defaultdict
from ctypes import Union
import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return-self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


def main():
    n, k, l = map(int, input().split())
    tree1 = UnionFind(n)
    tree2 = UnionFind(n)
    for _ in range(k):
        p, q = map(int, input().split())
        tree1.union(p-1, q-1)
    for _ in range(l):
        r, s = map(int, input().split())
        tree2.union(r-1, s-1)

    ans = {}
    for i in range(n):
        v = (tree1.find(i), tree2.find(i))
        if v not in ans:
            ans[v] = 1
        else:
            ans[v] += 1
    ans_l = []
    for i in range(n):
        v = (tree1.find(i), tree2.find(i))
        ans_l.append(ans[v])
    print(*ans_l)


if __name__ == '__main__':
    main()
