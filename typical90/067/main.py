def nbase_cvt(num, b_nums='012345678'):
    # if len(set(list(str(b_nums)))) != len(list(str(b_nums))):
    #     raise Exception('Please eliminate duplicate base numbers.')
    # if len(str(b_nums)) == 1:
    #     raise Exception('Set to binary or higher.')
    # if num != int(num) or num < 0:
    #     raise Exception('Please enter a positive integer for "num".')
    n = len(b_nums)

    res = ''
    while num >= n:
        idx = num % n
        res = b_nums[idx] + res
        num = int(num // n)
    idx = num % n
    res = b_nums[idx] + res
    return res


def tenbase_cvt(value, b_nums='01234567'):
    # if len(set(list(str(b_nums)))) != len(list(str(b_nums))):
    #     raise Exception('Please eliminate duplicate base numbers.')
    # if len(str(b_nums)) == 1:
    #     raise Exception('Set to binary or higher.')
    m = len(b_nums)
    num = 0
    for v in value:
        x = b_nums.find(v)
        # if x == -1:
        #     raise Exception(
        #         'Do not enter "value" that are not part of "b_nums".')
        num = num * m + int(x)
    return num


def main():
    n, k = map(int, input().split())
    for _ in range(k):
        n = str(n)
        n = int(str(nbase_cvt(int(tenbase_cvt(n)))).replace('8', '5'))
    print(n)


if __name__ == '__main__':
    main()
