mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [list(input()) for _ in range(n)]
    
    for i in range(n):
        for j in range(i, n):
            if li[i][j] == 'W' and li[j][i] != 'L':
                print('incorrect')
                exit()
            if li[i][j] == 'L' and li[j][i] != 'W':
                print('incorrect')
                exit()
            if li[i][j] == 'D' and li[j][i] != 'D':
                print('incorrect')
                exit()
    print('correct')

if __name__ == '__main__':
    main()
