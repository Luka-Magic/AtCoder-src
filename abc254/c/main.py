import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    li = [[] for _ in range(k)]
    for i, a in enumerate(A):
        li[i % k].append(a)
    

    for i in range(k):
        li[i].sort()
    ans = []
    for i in range(n):
        ans.append(li[i%k][i//k])
    
    
    for i in range(1, n):
        if ans[i-1] > ans[i]:
            print('No')
            exit()
    print('Yes') 





if __name__ == '__main__':
    main()
