from itertools import permutations, combinations

k = int(input())

li = [tuple(map(int, input().split())) for _ in range(k)]

for i in permutations(list(range(8)), 8):
    for a, b in li:
        if i[a] != b:
            break
    else:
        for j, k in combinations(list(range(8)), 2):
            x1, y1 = j, i[j]
            x2, y2 = k, i[k]
            if abs(x1 - x2) == abs(y1 - y2):
                break
        else:
            for a in range(8):
                ans = ''
                for b in range(8):
                    if i[a] != b:
                        ans += '.'
                    else:
                        ans += 'Q'
                print(ans)