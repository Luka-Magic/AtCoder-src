def main():
    h, w = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(h)]
    b = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            k = b[i][j] - a[i][j]
            a[i][j] += k
            a[i+1][j] += k
            a[i][j+1] += k
            a[i+1][j+1] += k
            ans += abs(k)
    for i in range(h):
        for j in range(w):
            if i != h-1 or j != w-1:
                continue
            if a[i][j] != b[i][j]:
                print('No')
                exit()
    print('Yes')
    print(ans)


if __name__ == '__main__':
    main()
