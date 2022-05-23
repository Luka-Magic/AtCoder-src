mod = 10**9 + 7
inf = float('inf')



def main():
    n = int(input())
    li = [input() for _ in range(n)]
    ans = inf

    for i in range(10): # 10
        di = {}
        for j in range(10):
            di[j] = 0
        for l in li: # 100
            for j, k in enumerate(l): # 10
                if int(k) == i:
                    di[j] += 1
                    break
        max_ = 0
        id_ = 0
        for j, count in di.items():
            if count >= max_:
                id_ = j
                max_ = count
        print(id_ + (max_ - 1) * 10)
        ans = min(id_ + (max_ - 1) * 10, ans)
    print(ans)

if __name__ == '__main__':
    main()
