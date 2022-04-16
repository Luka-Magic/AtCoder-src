import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def ten2n(num_10,n):
    li = []
    while num_10:
        li.append(num_10%n if num_10%n != 0 else 26)
        num_10 //= n
    return li

def main():
    n = int(input())
    ans = ''
    for i in ten2n(n, 26)[::-1]:
        ans += chr(i+ord('a')-1)
    print(ans)

if __name__ == '__main__':
    main()
