import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    
    
    low = -1
    high = 10**15
    while low + 1 < high:
        mid = (low + high) //2
        dead_li = [(mid - h) // s for h, s in li]
        dead_li.sort()
        flag = True
        for i, v in enumerate(dead_li):
            if i > v:
                flag = False
        if flag:
            high = mid
        else:
            low = mid
    print(high)

if __name__ == '__main__':
    main()
