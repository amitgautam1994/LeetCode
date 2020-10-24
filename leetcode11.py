# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

def longestConsecutive(nums):
    lookup = set(nums)
    seq_count = 0
    res = 0
    for num in lookup:
        seq_count = 1  # number itself
        if (num - 1 in lookup):  # skipping n=2 if n=1 is in the list, as we check n+1, n+2 .... for n = 1, where 2 will be included in it, so to prevent double check.
            continue
        while (num + 1 in lookup):
            seq_count += 1
            num = num + 1

        res = max(res, seq_count)
    return res

print("###############################")
print(longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print("###############################")
print(longestConsecutive([100, 4, 200, 1, 3, 2]))
print("###############################")
print(longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
