
mod = 10**9 + 7
inf = float('inf')
import math

def main():
    a, b = map(int, input().split())
    s = math.sqrt(a**2 + b**2)
    print(a/s, b/s)



if __name__ == '__main__':
    main()
