mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [list(input()) for _ in range(n)]
    incorrect_list = [('D', 'W'), ('D', 'L'), ('W', 'D'), ('L', 'D'), ('W', 'W'), ('L', 'L')]
    for i in range(n):
        for j in range(i, n):
            if i != j and (li[i][j], li[j][i]) in incorrect_list:
                print('incorrect')
                exit()
    print('correct')


if __name__ == '__main__':
    main()
