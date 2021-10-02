import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    s = int(input())
    h = s // 3600
    m = (s - h*3600) // 60
    ss = s % 60
    ans = str(h).zfill(2) + ':' + str(m).zfill(2) + ':' +str(ss).zfill(2)
    print(ans)



if __name__ == '__main__':
    main()
