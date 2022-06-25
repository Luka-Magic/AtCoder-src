import math
import sys
input = sys.stdin.readline

from itertools import product
mod = 10**9 + 7
inf = float('inf')


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt*2])

    if temp != 1:
        arr.append([temp, 2])

    if arr == []:
        arr.append([n, 2])

    return arr

def c(arr, k, u):
    a = [set() for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(0, arr[i][1]+1):
            a[i].add(arr[i][0]**j)
    re = 0
    for i in product(*a):
        p = 1
        for j in i:
            p *= j
        if p == u:
            re += 1
        if p <= k and p > u:
            re += 2
    return re



def main():
    n = int(input())
    ans = 0
    for i in range(1, n+1):
        ans += c(factorization(i), n, i)

    print(ans)

        


if __name__ == '__main__':
    main()
