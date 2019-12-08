def PrintMinNumber(numbers):
    # write code here
    nums = [str(c) for c in numbers]

    class st(str):
        def __lt__( x, y):
            return x + y < y + x

    nums.sort(key=st)
    res = ''.join(nums)
    return int(res)
nums = [3,32,321]
print(PrintMinNumber(nums))