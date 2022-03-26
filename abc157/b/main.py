import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    li = [list(map(int, input().split())) for _ in range(3)]
    li_ = [[0]*3 for _ in range(3)]
    q = int(input())
    for _ in range(q):
        a = int(input())
        for i in range(3):
            for j in range(3):
                if li[i][j] == a:
                    li_[i][j] = 1
    for i in range(3):
        if li_[i][0] + li_[i][1] + li_[i][2] == 3:
            print('Yes')
            exit()    
    for i in range(3):
        if li_[0][i] + li_[1][i] + li_[2][i] == 3:
            print('Yes')
            exit()
    if li_[0][0] + li_[1][1] + li_[2][2] == 3:
        print('Yes')
        exit()
    if li_[0][2] + li_[1][1] + li_[2][0] == 3:
        print('Yes')
        exit()
    print('No')



if __name__ == '__main__':
    main()
