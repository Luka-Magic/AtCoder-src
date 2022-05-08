mod = 10**9 + 7
inf = float('inf')

def ten2n(num_10,n):
    num_10 -= 1
    str_n = []
    while num_10:
        if len(str_n) == 0:
            str_n.append(num_10%n)
        else:
            str_n.append(num_10%n - 1)
        num_10 //= n
    return str_n[::-1]

def main():
    n = int(input())
    if n == 1:
        print('a')
    else:
        print(''.join([chr(i + ord('a')) for i in ten2n(n, 26)]))

if __name__ == '__main__':
    main()
