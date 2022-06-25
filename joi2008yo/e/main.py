import sys
input = sys.stdin.readline
import numpy as np
mod = 10**9 + 7
inf = float('inf')


def main():
    r, c = map(int, input().split())
    lines = []
    for i in range(r):
        line = list(map(int, input().split()))
        lines.append(line)
    lines = list(zip(*lines))
    print(lines)

if __name__ == '__main__':
    main()
