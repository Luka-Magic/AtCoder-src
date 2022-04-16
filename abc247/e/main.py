import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')

def main():
    n, x, y = map(int, input().split())
    li = list(map(int, input().split()))
    ans = 0
    max_l = [[]]
    min_l = [[]]
    l = [[]]
    su = 0
    for i in range(n):
        if li[i] < y or li[i] > x:
            su = i
            min_l.append([])
            max_l.append([])
            l.append([])
        else:
            if li[i] == y:
                min_l[-1].append(i - su)
            if li[i] == x:
                max_l[-1].append(i - su)
            l[-1].append(li[i])
    q = len(l)
    for j in range(q):
        right = 0
        flag = [False, False]
        if left in max_l[j]:
            flag[1] = True
        if left in min_l[j]:
            flag[0] = True
        for left in range(len(l[j])):

            while 1:
                right += 1
                    ans += len(l[j]) - right
                    break
    print(ans)

if __name__ == '__main__':
    main()
