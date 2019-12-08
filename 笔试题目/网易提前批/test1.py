import itertools

nums = [_ + 1 for _ in range(5)]
chazhao = (3,1,5,2,4)
A = list(itertools.permutations(nums))
ind = A.index(chazhao)
print(A[len(A)-1-ind])


