import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    nmax = 10**6+10

    ans = [0] * nmax

    for a in li:
        ans[a] += 1

    for i in range(nmax):
        if ans[i] == 0:continue
        if ans[i] > 1:ans[i] = 0
        for j in range(2*i, nmax, i):
            ans[j] = 0
    print(sum(ans))

if __name__ == '__main__':
    main()
