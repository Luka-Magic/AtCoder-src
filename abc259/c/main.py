from itertools import groupby

mod = 10**9 + 7
inf = float('inf')


def main():
    s = list(input())
    t = list(input())

    s_rl = [[key,len(list(group))] for key,group in groupby(s)]
    t_rl = [[key,len(list(group))] for key,group in groupby(t)]
    s_l = len(s_rl)
    t_l = len(t_rl)
    if s_l != t_l:
        print('No')
        exit()
    for i in range(s_l):
        s_str, s_num = s_rl[i]
        t_str, t_num = t_rl[i]
        if s_str != t_str:
            print('No')
            exit()
        if (s_num == 1) and (t_num > 1):
            print('No')
            exit()
        if (s_num > t_num):
            print('No')
            exit()
    print('Yes')

if __name__ == '__main__':
    main()
