import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    k = int(input())
    li = []
    def f(s, n):
        li.append(int(s))
        if n == 10:
            return
        i = int(s[0])
        if i - 1 >= 0:
            f(str(i-1) + s, n+1)
        f(str(i) + s, n+1)
        if i + 1 <= 9:
            f(str(i+1) + s, n+1)
    for i in range(10):
        f(str(i), 1)
    li = list(set(li))
    li.sort()
    print(li[k])


if __name__ == '__main__':
    main()
