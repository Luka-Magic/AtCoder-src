import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

from collections import deque

def main():
    q = int(input())
    que = deque([])
    for _ in range(q):
        inp = list(map(int, input().split()))
        if inp[0] == 1:
            que.append([inp[1], inp[2]])
        elif inp[0] == 2:
            m = inp[1]
            ret = 0
            while 1:
                x, c = que.popleft()
                if m > c:
                    m -= c
                    ret += c * x
                else:
                    que.appendleft([x, c-m])
                    print(ret + x * m)
                    break

if __name__ == '__main__':
    main()
