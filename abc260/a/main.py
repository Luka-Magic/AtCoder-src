mod = 10**9 + 7
inf = float('inf')

from collections import Counter
def main():
    s = list(input())
    c = Counter(s)
    for i, v in c.items():
        if v == 1:
            print(i)
            exit()
    print(-1)




if __name__ == '__main__':
    main()
