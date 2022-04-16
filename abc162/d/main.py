mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    s = list(input())
    from collections import Counter
    c = Counter(s)
    ans = 1
    if n == 1 or n == 2:
        print(0)
        exit()
    for i in c.values():
        ans *= i
    if len(c) != 3:
        print(0)
        exit()
    for i in range(n):
        for j in range(i+1, n):
            k = j + (j-i)
            if k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans -= 1
    print(ans)

if __name__ == '__main__':
    main()
