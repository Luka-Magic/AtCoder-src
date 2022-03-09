def main():
    n, q = map(int, input().split())
    li_ = list(map(int, input().split()))
    li = [li_[i] - li_[i-1] for i in range(1, n)]
    s = sum([abs(i) for i in li])
    for _ in range(q):
        l_, r_, v = map(int, input().split())
        if l_ == 1:
            l = -1
        else:
            l = l_ - 2
        if r_ == n:
            r = -1
        else:
            r = r_ - 1

        if l != -1:
            s += abs(li[l]+v) - abs(li[l])
            li[l] += v
        if r != -1:
            s += abs(li[r]-v) - abs(li[r])
            li[r] -= v
        print(s)


if __name__ == '__main__':
    main()
