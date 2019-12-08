def isValid(s):

    dic = {')': '(', '}': '{', ']': '['}
    stack = []
    for i in s:
        if i in dic:
            element = stack.pop() if stack else '#'
            if element != dic[i]:
                return False
        else:
            stack.append(i)
    return True if not stack else False


################最长的有效括号#################32

def longestValidParentheses( s):
    if not s:
        return 0
    res = 0
    stack = [-1]
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                res = max(res, i - stack[-1])
    return res

if __name__ == '__main__':
    s = ')()())'
    print(longestValidParentheses(s))
