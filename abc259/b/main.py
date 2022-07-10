import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

import math
import numpy as np

def main():
    a, b, d = map(int, input().split())
    r = np.array([[a, b]]).T
    R = np.array([[math.cos(d/180*np.pi), -math.sin(d/180*np.pi)], [math.sin(d/180*np.pi), math.cos(d/180*np.pi)]])
    a = np.dot(R, r)
    print(*a.T[0].tolist())

if __name__ == '__main__':
    main()
