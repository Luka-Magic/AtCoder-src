import math


def main():
    a, b, c = map(int, input().split())

    k = math.gcd(math.gcd(a, b), c)

    print((a-k) // k + (b-k) // k + (c-k) // k)

if __name__ == '__main__':
    main()
