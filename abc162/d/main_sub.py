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
    for inter in range(1, (n - 1)//2 + 1):
        start = 0
        while start + 2*inter < n:
            if (s[start] != s[start + inter]) and (s[start] != s[start + 2*inter]) and (s[start + inter] != s[start + 2*inter]):
                ans -= 1
            start += 1
    print(ans)

if __name__ == '__main__':
    main()
