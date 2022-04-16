def n2ten(num_n, n, m):
    num_10 = 0
    for s in str(num_n):
        num_10 *= n
        num_10 += int(s)
        if num_10 > m:
            return True
    return num_10

x = input()
m = int(input())

init = max(list(map(int, list(x))))+1
low = init - 1
high = 10**18 + 1

if len(x) == 1 and int(x) <= m:
    print(1)
    exit()

def f(mid):
    return n2ten(x, mid, m)

while low+1 < high:
    mid = (low + high) //2
    guess = f(mid)
    if guess > m or guess == True:
        high = mid
    else:
        low = mid
print(low - init + 1)