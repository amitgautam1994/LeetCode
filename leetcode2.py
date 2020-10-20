def findMedianSortedArrays(nums1, nums2):
    for i in nums2:
        nums1.append(i)

    nums1.sort()
    print(nums1)

    if len(nums1) % 2 == 0:
        mid = int((len(nums1) / 2) - 1)

        return (nums1[mid] + nums1[mid + 1]) / 2

    elif len(nums1) % 2 == 1:
        mid = int(((len(nums1) + 1) / 2) - 1)
        return nums1[mid]

print(findMedianSortedArrays([1,2],[3,4]))