import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    from itertools import permutations
    for idx, i in enumerate(permutations(list(range(1, n+1)), n)):
        if p == list(i):
            ans1 = idx
        if q == list(i):
            ans2 = idx
    print(abs(ans1-ans2))

if __name__ == '__main__':
    main()
