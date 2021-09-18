def main():
    n, l = map(int, input().split())
    K = int(input())
    li = list(map(int, input().split()))
    
    score = l // 2

    while d == 0:
        k = 0
        t = 0
        for i, l in enumerate(li):
            if l - k >= score:
                k = l
                t += 1
            if k >= score:
                k = 0
                t += 1
                if t >= K:
                    nokori = al - now
                    if nokori >= score:
                        score += score // 2
                        d = d//2
                        break
                    else:
                        score -= score // 2
                        d = d//2
                        break
        else:
            score -= score // 2
            d = d // 2
    print(d)


if __name__ == '__main__':
    main()
