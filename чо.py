a = input()


def qq(a):
    b = 0
    for i in a:
        if i.isdigit():
            b += 1
    if a[0] != '8' or a[0:2] != '+7' or a[-1] == '-' or a.count('(') != a.count(')') or b != 10:
        return 0
    return 1