import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, m = map(int, input().split())
    dic = dict()
    for _ in range(m):
        s, c =map(int, input().split())
        if n > 1 and s == 1 and c == 0:
            print(-1)
            exit()
        if s not in dic:
            dic[s] = c
        else:
            if dic[s] != c:
                print(-1)
                exit()
            else:
                continue
    for i in range(10**(n-1) if n != 1 else 0, 10**n):
        v = str(i)
        for a, b in dic.items():
            if v[a-1] != str(b):
                break
        else:
            print(i)
            exit()

if __name__ == '__main__':
    main()
