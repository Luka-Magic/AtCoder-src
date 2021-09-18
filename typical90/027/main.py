def main():
    n = int(input())
    u_l = set()
    for i in range(1, n+1):
        user = input()
        if user not in u_l:
            print(i)
            u_l.add(user)

if __name__ == '__main__':
    main()
