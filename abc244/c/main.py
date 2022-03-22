import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    all = set()

    for _ in range(2*n+1):
        for i in range(1, 2*n+2):
            if i not in all:
                print(i, flush=True)
                all.add(i)
                break
        t = int(input())
        all.add(t)


if __name__ == '__main__':
    main()
