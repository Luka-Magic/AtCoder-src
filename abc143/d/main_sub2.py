import sys
input = sys.stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                ans += (li[k] < li[j] + li[i])
    print(ans)

if __name__ == '__main__':
    main()
