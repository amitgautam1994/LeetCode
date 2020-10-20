# Remove Duplicates from Sorted Array

def removeDuplicates(nums):
    size = len(nums) - 1

    while size >= 0:
        if nums[size] in nums[:size]:
            nums.pop(size)

        size -= 1

    return nums


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
