s = input() + 'R'

init = 0
mid = None
last = None
flag = False
ans = []
for i, k in enumerate(s):
    if k == 'L' and not flag:
        mid = i - init
        flag = True
    if k == 'R' and flag:
        last = i - init - 1
        ans_t = [0] * (last + 1)
        if (last+1) % 2 == 0:
            ans_t[mid], ans_t[mid-1] = (last+1) // 2, (last+1) // 2
        else:
            if mid % 2 == 1:
                ans_t[mid], ans_t[mid-1] = (last+1) // 2, (last+1) // 2 + 1
            else:
                ans_t[mid], ans_t[mid-1] = (last+1) // 2 + 1, (last+1) // 2
        ans.extend(ans_t)
        flag = False
        init = i
        mid, last = None, None

print(*ans)
