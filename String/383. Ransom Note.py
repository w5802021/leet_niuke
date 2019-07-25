
def canConstruct(ransomNote, magazine):
    if len(ransomNote) > len(magazine):
        return False
    for i in set(ransomNote):
        if ransomNote.count(i) > magazine.count(i):
            return False
    return True

if __name__ == '__main__':
    ransomNote,magazine= "aa","aab"
    print(canConstruct(ransomNote, magazine))