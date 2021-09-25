def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


def main():
    n = int(input())
    arr = factorization(n)
    k = sum([x[1] for x in arr])
    if k == 1:
        print(0)
        exit()
    print(len(bin(k-1))-2)


if __name__ == '__main__':
    main()
