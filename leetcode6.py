def check(nums, k):
    lst = nums[len(nums) - k:]
    for i in nums[:k+1]:
        lst.append(i)

    return lst


print(check([1,2,3,4,5,6,7], 3))