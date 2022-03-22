from collections import deque
mod = 10**9 + 7
inf = float('inf')


def main():
    n, x = map(int, input().split())
    s = list(input())
    x = list(bin(x)[2:])
    que = deque(x)

    for i in range(n):
        if s[i] == 'U':
            que.pop()
        elif s[i] == 'L':
            que.append('0')
        elif s[i] == 'R':
            que.append('1')
    print(int(''.join(list(que)), 2))

if __name__ == '__main__':
    main()
