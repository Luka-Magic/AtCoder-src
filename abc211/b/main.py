# import sys
# input = sys.stdin.readline


def main():
    li = ['H', '3B', 'HR', '2B']
    l = []
    for _ in range(4):
        l.append(input())
    li.sort()
    l.sort()
    # print(li)
    # print(l)

    for i in range(4):
        if li[i] != l[i]:
            print('No')
            exit()
    else:
        print('Yes')


if __name__ == '__main__':
    main()
