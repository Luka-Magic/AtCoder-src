mod = 2019
inf = float('inf')

def main():
    s = list(input())
    c = [0] * 2019
    c[0] = 1
    now = 0
    ans = 0
    for i in range(len(s)):
        now += int(s[len(s)-i-1]) * pow(10, i, mod)
        now %= mod
        c[now] += 1
        ans += c[now] - 1
    print(ans)

if __name__ == '__main__':
    main()
