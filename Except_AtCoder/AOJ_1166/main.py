while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    masu = [[0] * (2*w-1) for _ in range(2*h-1)]
    for i in range(2*h-1):
        walls = map(int, input().split())
        if i % 2 == 0:
            for j, wall in enumerate(walls):
                if wall == 1:
                    masu[i][2*j+1] = 1
                    if i > 0:
                        masu[i-1][2*j+1] = 1
                    elif i < 2*h-1:
                        masu[i+1][2*j+1] = 1
        else:
            for j, wall in enumerate(walls):
                if wall == 1:
                    masu[i][2*j] = 1
                    if j > 0:
                        masu[i][2*j-1] = 1
                    elif j < 2*w-2:
                        masu[i][2*j+1] = 1
    # for l in masu:
    #     print(*l)

    seen = [[0]*(2*w-1) for _ in range(2*h-1)]
    seen[0][0] = 1
    from collections import deque
    que = deque([(0, 0)])
    while que:
        x, y = que.popleft()
        if x == 2*w-2 and y == 2*h-2:
            break
        for px, py in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nx = x + px
            ny = y + py
            if 0 <= nx < 2*w-1 and 0 <= ny < 2*h-1:
                if masu[ny][nx] == 1:
                    continue
                nx += px
                ny += py
                if seen[ny][nx] == 0 and masu[ny][nx] == 0:
                    seen[ny][nx] = seen[y][x] + 1
                    que.append((nx, ny))
    print(seen[2*h-2][2*w-2])
