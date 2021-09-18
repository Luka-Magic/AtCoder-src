def main():
    n = int(input())
    al = list(map(int, input().split()))
    bl = list(map(int, input().split()))
    al.sort()
    bl.sort()
    ans = 0
    for i, j in zip(al, bl):
        ans += abs(j-i)
    print(ans)

if __name__ == '__main__':
    main()
