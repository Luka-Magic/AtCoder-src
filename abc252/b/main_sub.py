import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    idx = []
    ans = 0
    for i, a in enumerate(A):
        if a > ans:
            idx.clear()
            idx.append(i+1)
            ans = a
        elif a == ans:
            idx.append(i+1)
    for id_ in idx:
        if id_ in B:
            print('Yes')
            exit()
    print('No')




if __name__ == '__main__':
    main()
