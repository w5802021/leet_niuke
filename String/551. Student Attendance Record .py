
def checkRecord(s):
    if s.count('A') > 1:
        return False
    for i in range(2, len(s)):
        if s[i] == 'L' and s[i - 1] == 'L' and s[i - 2] == 'L':
            return False
    return True

if __name__ == '__main__':
    s = "PPALLP"
    print(checkRecord(s))