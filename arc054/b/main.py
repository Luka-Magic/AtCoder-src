def main():
    p = float(input())

    def f(x):
        return x + (p / pow(2., x / 1.5))

    low, high = 0., 100.

    while high - low > 1e-8:
        c1 = (low * 2 + high) / 3. 
        c2 = (low + high * 2) / 3. 
        y1 = f(c1)
        y2 = f(c2)
        if y1 > y2:
            low = c1
        else:
            high = c2
    print(f(low))

if __name__ == '__main__':
    main()
