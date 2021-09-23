import bisect
import sys
input = sys.stdin.readline


def main():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n**0.5//1))+1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])

        if arr == []:
            arr.append([n, 1])

        arr = list(map(lambda x: x[0], arr))

        return arr
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    s = set()
    no = set()
    for i in li:
        t = factorization(i)
        for j in t:
            s.add(j)

    for i in s:
        if i == 1:
            continue
        for p in range(1, m+1):
            if p * i > m:
                break
            no.add(p*i)
    no = list(no)
    no.sort()
    nl = len(no)
    ans = []
    for i in range(1, m+1):
        k = bisect.bisect_left(no, i)
        if no[k] == i:
            continue
        ans.append(i)
    print(len(ans))
    for i in ans:
        print(i)


if __name__ == '__main__':
    main()
