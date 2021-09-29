import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def tenbase_cvt(value, b_nums):
    m = len(b_nums)
    num = 0
    for v in value:
        x = b_nums.find(v)
        if x == -1:
            raise Exception(
                'Do not enter "value" that are not part of "b_nums".')
        num = num * m + int(x)
    return num


def main():
    k = int(input())
    a, b = map(int, input().split())
    t = ''.join([str(x) for x in range(k)])
    print(tenbase_cvt(str(a), t) * tenbase_cvt(str(b), t))


if __name__ == '__main__':
    main()
