import re
while True:
    s = input()
    ser1 = input()
    ser2 = input()
    # 正则表达式  通配符
    p = '.*' + ser1 + '.*' + ser2 + '.*'
    patt = re.compile(p)
    if patt.match(s):
        if patt.match(s[::-1]):
            print('both')
        else:
            print('forward')
    elif patt.match(s[::-1]):
        print('backward')
    else:
        print('invalid')

