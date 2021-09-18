import sys
input = sys.stdin.readline


def main():
    li = list(map(int, input().split()))
    su = sum(li)
    ma = max(li)
    if su % 2 == ma % 2:print((ma*2-(su-ma))//2)
    else:print(((ma+1)*2-(su-ma)+1)//2)

if __name__ == '__main__':
    main()
