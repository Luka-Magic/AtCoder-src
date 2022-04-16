mod = 10**9 + 7
inf = float('inf')


def main():
    x = int(input())
    i = 1
    while x >= 2 * i**5:
        i += 1
    for j in range(-1*i, i+1):
        if i**5 - j**5 == x:
            print(i, j)
            exit()

if __name__ == '__main__':
    main()
