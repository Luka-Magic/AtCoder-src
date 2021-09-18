def main():
    n = int(input())
    a, b, c = map(int, input().split())

    ans = 100000

    for i in range(10000):
        for j in range(10000 - i):
            p = (n - (i*a + j*b))
            if p < 0:
                continue
            if (n - (i*a + j*b)) % c == 0:
                k = (n - (i*a + j*b)) // c
                ans = min(i+j+k, ans)
    
    print(ans)


if __name__ == '__main__':
    main()
