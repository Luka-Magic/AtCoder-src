import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')
import re

def main():
    print(max(map(len, re.split('[^ACGT]', input()))))

if __name__ == '__main__':
    main()
