def match(s,p):    #暴力匹配法
    i = 0
    j = 0
    lens = len(s)
    lenp = len(p)
    if lens < lenp:
        return False

    while i < lens and j < lenp:
        if s[i] == p[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1             #回朔
            j = 0
            if i > lens - lenp:
                return False
    if j >= lenp:
        return i - lenp

    return False

#########################################################################
def get_next(p,nexts):
    i = 0
    j = -1
    nexts[0] = -1
    while i < len(p):
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            nexts[i] = j
        else:
            j = nexts[j]

    return nexts

def match2(s,p):
    i = 0
    j = 0
    lens = len(s)
    lenp = len(p)

    nexts = [0]*(lenp+1)
    nexts = get_next(p,nexts)

    if lens < lenp:
        return False

    while i < lens and j < lenp:
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = nexts[j]
    if j >= lenp:
        return i - lenp

    return False


if __name__ == '__main__':
    s = 'abababaabcbab'
    p = 'abaabc'

    print(match2(s,p))
