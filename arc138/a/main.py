import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    li = list(map(int, input().split()))
    A = []
    B = []
    for i in range(k):
        A.append([li[i], i])
    for j in range(k, n):
        B.append([li[j], j])
    A.sort(key=lambda x: x[1], reverse=True)
    B.sort(key=lambda x: x[1], reverse=True)
    A.sort(key=lambda x: x[0], reverse=True)
    B.sort(key=lambda x: x[0], reverse=False)

    p = n-k-1
    min_r = inf
    ans = inf
    # print(min(A, key=lambda x: x[0]))
    # print(max(B, key=lambda x:x[0]))
    if min(A, key=lambda x:x[0])[0] >= max(B, key=lambda x:x[0])[0]:
        print(-1)
        exit()
    
    for i in range(k):
        a, l = A[i]
        # print(a, l)
        while p+1:
            b, r = B[p]
            # print(b, r)
            if a < b:
                p -= 1
                min_r = min(min_r, r)
                ans = min(ans, min_r - l)
            else:
                break
        ans = min(ans, min_r - l)
        # print(i, p, min_r, ans)
    print(ans)


if __name__ == '__main__':
    main()
