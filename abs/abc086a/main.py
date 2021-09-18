def main():
    a, b = map(int, input().split())
    ans = 'Odd'
    if a * b % 2 == 0:
        ans = 'Even'
    print(ans)


if __name__ == '__main__':
    main()
