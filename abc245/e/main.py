import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    cho = [[a, b] for a, b in zip(A, B)]
    hako = [[a, b] for a, b in zip(C, D)]
    cho.sort(key=lambda x:x[0], reverse=True)
    hako.sort(key=lambda x:x[0], reverse=True)
    if n > m:
        print('No')
        exit()
    s, t = 0, 0
    seen = [0] * n
    while t < m-1:
        c, d = hako[t]
        a, b = cho[s]
        if a <= c:
            if b <= d:
                t += 1
                while 1:
                    if not seen[s+1]:
                        s += 1
                        break
                    else:
                        s += 1
            else:
                k = s + 1
                while 1:
                    a_, b_ = cho[k]
                    if b_ <= d and not seen[k]:
                        seen[k] = 1
                        break
                    else:
                        k += 1
        else:
            print('No')
            exit()
    print('Yes')
    
                    
                    
                    







if __name__ == '__main__':
    main()
