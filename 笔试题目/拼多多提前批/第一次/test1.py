def main(numa, numb):
    '''
    题意：给定两个列表numa、numb，numa中有一个数字不遵循列表严格单调上升，在
         numb中找出一个最大的数，使得列表numa严格单调上升，
    未全AC原因：没有注意列表中需要修改的数字出现在列表边缘的情况,
                numa = [1 ,3, 7, 8, 6]，numb = [2, 1, 5, 8, 9] （不符合条件的数出现在列表头）
                numa = [5 ,3, 7, 8, 6]，numb = [2, 1, 5, 8, 9] （不符合条件的数出现在列表尾）
               没有考虑numa[i]未能找到合适替换数，应该想办法替换numa[i-1]
    :param numa:
    :param numb:
    :return:numa修改后的列表输出，如果没找到则输出NO
    '''
    # 未能全部通过原因，没有考虑numa边界
    numa.append(float('inf'))
    numa.insert(0,float('-inf'))
    # 先拿较大的数来替换
    numb.sort(reverse=True)

    for i in range(1,len(numa)):
        if numa[i] > numa[i - 1]:
            continue
        else:
            # 先想办法替换numa[i]，若未能找到，则再想办法替换numa[i+1]，如果都不能找到值，则输出NO
            for j in range(len(numb)):
                if numa[i-1] < numb[j] < numa[i + 1]:
                    numa[i] = numb[j]
            for j in range(len(numb)):
                if numa[i - 2] < numb[j] < numa[i]:
                    numa[i-1] = numb[j]
            numa.pop(0)
            numa.pop(-1)
            str1 = ''
            for i in numa:
                str1 = str1 + ' ' + str(i)
            return str1.lstrip(' ')
    return 'NO'

if __name__ == '__main__':
    numa = [1 ,3, 7, 8, 7]
    numb = [2, 1, 5, 8, 9]
    print(main(numa, numb))