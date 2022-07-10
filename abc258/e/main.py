from itertools import accumulate

def main():
    n, q, x = map(int, input().split())
    li = list(map(int, input().split()))
    c_li = list(accumulate(li))
    sum_li = c_li[-1]
    dic = {}
    now = 0
    l = []
    while 1:
        value = (x + c_li[now - 1]) % sum_li
        low = -1
        high = len(li) - 1
        while low + 1 < high:
            mid = (low + high) // 2
            guess = c_li[mid]
            if guess > value:
                high = mid
            else:
                low = mid
        if now in dic.keys():
            p = l.index(now)
            break
        dic[now] = (high + 1 - now + (x // sum_li)) % n
        l.append(now)
        now = (high + 1) % n
    for _ in range(q):
        k = int(input()) - 1
        if k < p:
            print(dic[k])
        else:
            len_ = len(l)
            a = k % (len_ - p)
            print(p + dic[a])

if __name__ == '__main__':
    main()
