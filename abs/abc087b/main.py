def main():
    A = int(input())
    B = int(input())
    C = int(input())
    x = int(input())

    k = 0
    for a in range(A+1):
        for b in range(B+1):
            for c in range(C+1):
                if x == 500*a+100*b+50*c:
                    k += 1
    print(k)


if __name__ == '__main__':
    main()
