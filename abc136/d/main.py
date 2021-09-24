s = input()
ans = [0] * len(s)
for _ in range(2):
    count = 0
    for i, k in enumerate(s):
        if k == 'R':
            count += 1
            continue
        if k == 'L':
            ans[i-1] += (count + 1) // 2
            ans[i] += count // 2
            count = 0

    ans = ans[::-1]
    s = s[::-1]
    s = ''.join(['R' if i == 'L' else 'L' for i in s])
print(*ans)
