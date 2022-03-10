mod = 10**9 + 7
inf = float('inf')


def main():
    li = ['Sunny', 'Cloudy', 'Rainy']
    s = input()
    for i, l in enumerate(li):
        if s == l:
            print(li[(i+1) % 3])
            break


if __name__ == '__main__':
    main()
