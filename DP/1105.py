def minHeightShelves(books, shelf_width):
    '''
    动态规划
    思路：每放入一本书，将其放入新起的一层，随后不断将之前已经摆好的书往新起的一层后移，在保证新起的一层不超过最大宽度的前提下，
         递推得到最小的书架整体高度
    :param books:
    :param shelf_width:
    :return:
    '''
    n = len(books)
    # dp[i]表示第i本书放入书架的整体最小高度
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    for i in range(1,n+1):
        # tmp_width 当前新层宽度，j为第i本书及其之前已经摆放的书
        tmp_width,j,h = 0,i,0
        while j > 0 :
            tmp_width += books[j-1][0]
            if tmp_width > shelf_width:
                break
            # 本层最大高度的书作为本层高度
            h = max(h, books[j-1][1])
            dp[i] = min(dp[i],dp[j-1]+h)
            j -= 1
    return dp[-1]

if __name__ == '__main__':
    books = [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]]
    shelf_width = 4
    print(minHeightShelves(books,shelf_width))