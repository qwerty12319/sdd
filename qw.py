def qq(a):
    b = 0
    c = ''
    for i in a:
        if i.isdigit():
            b += 1
            c += i
    if a[0] != '8' and a[0:2] != '+7' or a[-1] == '-' or a.count('(') != a.count(')') or b != 11 or '--' in a:
        return 'error'
    return '+7' + c[1:]


print(qq(input()))