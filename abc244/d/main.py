mod = 10**9 + 7
inf = float('inf')


def main():
    s = list(map(str, input().split()))
    t = list(map(str, input().split()))

    if s == t:
        print('Yes')
    elif [s[1], s[2], s[0]] == t:
        print('Yes')
    elif [s[2], s[0], s[1]] == t:
        print('Yes')
    elif [s[2], s[1], s[0]] == t:
        print('No')
    elif [s[1], s[0], s[2]] == t:
        print('No')
    elif [s[0], s[2], s[1]] == t:
        print('No')

if __name__ == '__main__':
    main()
