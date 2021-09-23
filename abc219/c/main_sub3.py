x = input()
n = int(input())
s = [input() for _ in range(n)]

t = {}
for i in range(26):
    t[x[i]] = chr(i + ord('a'))

print(*sorted(s, key=lambda x: ''.join(t[c] for c in x)), sep='\n')
