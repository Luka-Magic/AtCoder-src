mod = 10**9 + 7
inf = float('inf')

def main():
    s = input()
    flag = 0
    q = int(input())
    mae = []
    usiro = []
    for _ in range(q):
        query = list(map(str, input().split()))
        if query[0] == '1':
            flag += 1
            flag %= 2
        else:
            _, f, c = query
            k = flag^int(f)-1
            if k == 0:
                mae.append(c)
            else:
                usiro.append(c)
    s = ''.join(mae[::-1]) + s + ''.join(usiro)
    if flag == 1:
        s = s[::-1]
    print(s)

if __name__ == '__main__':
    main()
