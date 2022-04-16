import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    k = int(input())
    from collections import deque
    que = deque([1, 2, 3, 4, 5, 6, 7, 8, 9])
    now = 0
    while now != k:
        t = que.popleft()
        now += 1
        for i in [-1, 0, 1]:
            last = t % 10
            add = last + i
            if add < 0 or add > 9:continue
            que.append(int(str(t) + str(add)))
    print(t)

if __name__ == '__main__':
    main()
