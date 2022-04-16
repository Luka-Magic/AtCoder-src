def main():
    n = int(input())
    li = list(map(int, input().split()))
    dp = [0] * n
    dp[0] = li[0] - 1
    for i in range(1, n):
        if dp[i-1] < li[i]:
            dp[i] = li[i] - 1
        elif dp[i-1] == li[i]:
            dp[i] = li[i]
        else:
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()
