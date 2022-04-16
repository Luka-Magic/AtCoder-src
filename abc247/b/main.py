mod = 10**9 + 7
inf = float('inf')

def main():
    n = int(input())
    li = [list(input().split()) for _ in range(n)]
    
    for i, (a, b) in enumerate(li):
        pre = False
        post = False
        for j, (s, t) in enumerate(li):
            if j == i:continue
            if s == a:
                pre = True
            if t == a:
                pre = True
            if s == b:
                post = True
            if t == b:
                post = True
        if (pre == True) and (post == True):
            print('No')
            exit()
    print('Yes') 


if __name__ == '__main__':
    main()
