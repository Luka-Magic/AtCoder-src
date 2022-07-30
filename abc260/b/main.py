import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, x, y, z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    g = []

    A_ = [[i, v] for i, v in enumerate(A)]

    A_.sort(key=lambda x: x[1], reverse=True)
    for i in range(x):
        g.append(A_[i][0])

    B_ = [[i, v] for i, v in enumerate(B) if i not in g]
    B_.sort(key=lambda x: x[1], reverse=True)
    for j in range(y):
        g.append(B_[j][0])
    
    C_ = [[i, a+b] for i, (a, b) in enumerate(zip(A, B)) if i not in g]
    C_.sort(key=lambda x: x[1], reverse=True)
    for k in range(z):
        g.append(C_[k][0])
    g.sort()
    for i in g:
        print(i + 1)

if __name__ == '__main__':
    main()
