import sys
import math
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    s = input()
    q = int(input())
    max_n = int(math.log2(10**18)) + 1
    for _ in range(q):
        t, k = map(int, input().split())
        if t > max_n:
            m = 0
            l = bin(k-1)[2:]
        else:
            m = (k-1) // 2**t
            l = bin((k-1) % 2**t)[2:]
        top = ord(s[m])-65
        a = l.count('1') % 3
        b = (t - a) % 3
        print(chr((top - a + b) % 3 + 65))

if __name__ == '__main__':
    main()
