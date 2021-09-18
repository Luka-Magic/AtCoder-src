import math


def main():
    def lcm(a, b):
        y = a*b // math.gcd(a, b)
        return y

    a, b = map(int, input().split())
    l = lcm(a, b)
    if l > 10**18:
        print('Large')
    else:
        print(l)


if __name__ == '__main__':
    main()
