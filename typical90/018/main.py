import math

def main():
    t = int(input())
    l, x, y = map(int, input().split())
    q = int(input())
    for _ in range(q):
        e = int(input())
        y_ = (-l/2) * math.sin(math.radians(360 * e / t))
        c = (-l/2) * math.cos(math.radians(360 * e / t)) + (l/2)
        a = math.sqrt((y_ - y)**2 + x**2)
        theta = math.degrees(math.atan(c / a))
        print(theta)


if __name__ == '__main__':
    main()
