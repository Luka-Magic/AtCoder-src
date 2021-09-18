def kai(b):
    l = len(b)
    lef = b[:(l-1)//2][::-1]
    rig = b[(l+1)//2:]
    if lef == rig:
        return True
    else:
        return False


def main():
    s = input()
    if kai(s):
        l = len(s)
        if kai(s[:(l-1)//2]) and kai(s[(l+1)//2:]):
            print('Yes')
        else:
            print('No')
    else:
        print('No')


if __name__ == '__main__':
    main()
