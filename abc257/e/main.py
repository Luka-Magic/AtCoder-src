import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')



def main():
    n = int(input())
    li = list(map(int, input().split()))

    ans = 0
    m = 0
    m_l = 0
    for l in li:
        if m <= (n // l):
            m_l = l
            m = n // l
    ans_l = [l] * m
    min_ = min(li)
    nokori = n - (l * m)
    now = 0
    for i in range(9):
        j = 9 - i
        while 1:
            if nokori >= li[j-1] - min_:
                ans_l[now] = j
                nokori -= li[j-1] - min_
            else:
                break
    ans = ans_l[0]
    for i in ans_l[1:]:
        ans = ans * 10 + i

if __name__ == '__main__':
    main()
