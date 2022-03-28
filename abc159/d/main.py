import collections
import sys
input = sys.stdin.readline

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n
    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result

def main():
    n = int(input())
    li = list(map(int, input().split()))
    
    from collections import Counter
    c = Counter(li)
    s = sum([cmb(i, 2) if i != 1 else 0 for i in c.values()])
    for i in li:
        print(s - c[i] + 1)

if __name__ == '__main__':
    main()
