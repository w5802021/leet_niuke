#归并排序思想：如果要排序一个数组，我们先把数组从中间递归地分成前后两部分。
#然后分别对前后两部分进行排序，再将排好序的两部分数据合并在一起就可以了
#
def mergesort(list):
    if len(list) <= 1:
        return list
    num = len(list)//2
    # 递归划分待排序的数组
    left = mergesort(list[:num])
    right = mergesort(list[num:])
    return merge(left,right)

def merge(left,right):
    l,r=0,0
    res = []

    while l < len(left) and r < len(right):
        # 将待合并的数组left、right合并，并进行排序（left、right数组已排序）
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1

    res += right[r:]
    res += left[l:]
    return res

if __name__ == '__main__':
    l = [1, 3, 2, 4, 5, 6, 7, 90, 21, 23, 45]
    print(mergesort(l))
