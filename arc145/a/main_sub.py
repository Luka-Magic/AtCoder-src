from re import A


n = int(input())
S = list(input())
s = S.copy()
can = False
for i in range(n//2):
    if s[i] == 'A' and s[n-i-1] == 'A':
        can = True
    if s[i] == 'A' and s[n-i-1] == 'B':
        if not can:
            break
    if s[i] == 'B' and s[n-i-1] == 'A':
        if n % 2 == 0 and i == n // 2 - 1:
            break
        else:
            s[i] = 'A'
            s[i+1] = 'B'
            can = False
    if s[i] == 'B' and s[n-i-1] == 'B':
        can = False
else:
    print('Yes')
    exit()

s = S[::-1]
can = False
for i in range(n//2):
    if s[i] == 'B' and s[n-i-1] == 'B':
        can = True
    if s[i] == 'B' and s[n-i-1] == 'A':
        if not can:
            break
    if s[i] == 'A' and s[n-i-1] == 'B':
        if n % 2 == 0 and i == n // 2 - 1:
            break
        else:
            s[i] = 'B'
            s[i+1] = 'A'
            can = False
    if s[i] == 'A' and s[n-i-1] == 'A':
        can = False
else:
    print('Yes')
    exit()
print('No')