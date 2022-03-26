import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

from collections import defaultdict
class UnionFind():
    def __init__(self, n):
        self.n= n
        self.parents= [-1]* n
    def find(self, x):
        if self.parents[x]< 0:
            return x
        else:
            self.parents[x]= self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x= self.find(x)
        y= self.find(y)
        if x== y:
            return
        if self.parents[x]> self.parents[y]:
            x, y= y, x
        self.parents[x]+= self.parents[y]
        self.parents[y]= x
    def size(self, x):
        return-self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x)== self.find(y)
    def members(self, x):
        root= self.find(x)
        return [i for i in range(self.n) if self.find(i)== root]
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x< 0]
    def group_count(self):
        return len(self.roots())
    def all_group_members(self):
        group_members= defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

def main():
    n, m, k = map(int, input().split())
    tree = UnionFind(n)
    friends = dict()
    for _ in range(m):
        a, b = map(int, input().split())
        tree.union(a-1, b-1)
        if a-1 not in friends:
            friends[a-1] = set([b-1])
        else:
            friends[a-1].add(b-1)
        if b-1 not in friends:
            friends[b-1] = set([a-1])
        else:
            friends[b-1].add(a-1)
    blocks = dict()
    for _ in range(k):
        c, d = map(int, input().split())
        if c-1 not in blocks:
            blocks[c-1] = set([d-1])
        else:
            blocks[c-1].add(d-1)
        if d-1 not in blocks:
            blocks[d-1] = set([c-1])
        else:
            blocks[d-1].add(c-1)
    ans = [0 for _ in range(n)]
    for mems in tree.all_group_members().values():
        mem = set(mems)
        l = len(mems)
        for i in mems:
            l_i = l - 1
            if i in friends:
                for j in friends[i]:
                    if j in mem:
                        l_i -= 1
            if i in blocks:
                for j in blocks[i]:
                    if j in mem:
                        l_i -= 1
            ans[i] = l_i
    print(*ans)

if __name__ == '__main__':
    main()
