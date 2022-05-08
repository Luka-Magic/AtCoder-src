mod = 10**9 + 7
inf = float('inf')

def ten2n(num_10, n, i):
    str_n = ''
    c = 0
    while num_10:
        str_n += chr(num_10 % n + ord('a'))
        num_10 //= n
        c += 1
    return 'a' * (i - c) + str_n[::-1]

def main():
    n = int(input())
    ans = ''
    i = 0
    k = n - 1
    while 1:
        if 0 <= k < 26 ** (i + 1):
            print(ten2n(k, 26, i+1))
            break
        else:
            k -= 26 ** (i + 1)
            i += 1

if __name__ == '__main__':
    main()
