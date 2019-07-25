def ispopserial(push,pop):

    if not push or not pop:
        return False
    pushlen = len(push)
    poplen = len(pop)
    if pushlen != poplen:
        return False

    pushind = 0
    popind = 0
    stack = []

    while pushind < pushlen:
        stack.append(push[pushind])
        pushind += 1
        # 没push一个元素就判断它是否可以被pop
        while stack and stack[-1] == pop[popind]:
            stack.pop()
            popind += 1
    return len(stack) == 0 and popind == poplen

if __name__ == '__main__':
    push = '12345'
    pop = '35412'
    print(ispopserial(push,pop))