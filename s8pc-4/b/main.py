import sys
input = sys.stdin.readline

mod = 10**9 + 7
inf = float('inf')


def main():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    ans = inf
    for i in range(2**n):
        c = 0
        k_ = 1
        max_ = 0
        new_li = [A[0]]
        m_ = new_li[0]
        for j in range(1, n):
            if (i >> j) & 1:
                if m_ >= A[j]:
                    c += (m_ - A[j] + 1)
                    new_li.append(m_ + 1)
                    m_ += 1
                else:
                    new_li.append(A[j])
                    m_ = A[j]
            else:
                new_li.append(A[j])
                if A[j] > m_:
                    m_ = A[j]
        m_ = new_li[0]
        for j in range(1, n):
            if new_li[j] > m_:
                k_ += 1
                m_ = new_li[j]
        if k_ >= k:
            ans = min(ans, c)

    print(ans)


if __name__ == '__main__':
    main()
