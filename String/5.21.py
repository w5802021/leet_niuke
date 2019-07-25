def isChinese(ch):
    return True if '\u4e00' <= ch <= '\u9af5' else False

def truncatestr(strs,lens):
    if strs == '' or strs== None or lens == 0:
        return ''
    sb = ''
    count = 0
    for c in strs:
        if count <lens:
            if isChinese(c):
                if count + 1 <= lens and count + 3 > lens:
                    return sb
                count += 3
                sb += c
            else:
                count += 1
                sb += c
        else:
            break
    return sb

if __name__ == '__main__':
    strs = '人ABC们DEF'
    lens = 6
    print(truncatestr(strs,lens))