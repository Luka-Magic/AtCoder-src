import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

# 参考提出コード https://atcoder.jp/contests/abc216/submissions/26114680


def main():
    n, m = map(int, input().split())
    li = []
    k = []
    for _ in range(m):
        k.append(int(input()))
        li.append(list(map(int, input().split())))
    from collections import deque
    que = deque()
    for i in range(m):
        que.append([i, 0])
    dic = {}
    # print(que)
    while que:
        print(que)
        a, b = que.popleft()
        c = li[a][b]
        # print(a, b, c)
        if c not in dic.keys():
            dic[c] = 1
        else:
            dic[c] = 0
            if k[a] == b + 1:
                continue
            que.append([a, b+1])
    # print(dic)
    if sum(dic.values()) == 1:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
