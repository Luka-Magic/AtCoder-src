s = {}
s[1] = input()
s[2] = input()
s[3] = input()

t = input()
print(''.join([s[int(i)] for i in t]))
