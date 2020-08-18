import math
def findMedianSortedArrays(nums1, nums2):
    # if brute force with O(m+n)
    # merge the 2 array then find the median
    if len(nums1) > len(nums2):
        findMedianSortedArrays(nums2,nums1)
    x = len(nums1)
    y = len(nums2)
    low = 0
    high = x
    while(low <= high):
        partitionX = int(round((low+high) / 2))
        partitionY = int(round((x + y + 1) / 2 - partitionX))
        if partitionX == 0:
            maxLeftX = -math.inf
        else:
            maxLeftX = nums1[partitionX - 1]
        if partitionX == x:
            minRightX = math.inf
        else:
            minRightX = nums1[partitionX]
        if partitionY == 0:
            maxLeftY = -math.inf
        else:
            maxLeftY = nums2[partitionY - 1]
        if partitionY == y:
            minRightY = math.inf
        else:
            minRightY = nums2[partitionY]
        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x+y) % 2 == 0:
                median = ( max(maxLeftX, maxLeftY) + min(minRightX, minRightY) ) / 2
            else:
                median = max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
    print("The median is {:.1f}".format(median))

nums1 = [1, 3]
nums2 = [2]
findMedianSortedArrays(nums1, nums2)

nums = [1, 2]
nums0 = [3, 4]
findMedianSortedArrays(nums, nums0)

nums3 = [1, 3]
nums4 = [2, 4, 6]
findMedianSortedArrays(nums3, nums4)

nums5 = [1, 3, 5, 7, 9]
nums6 = [2, 4, 6]
findMedianSortedArrays(nums5, nums6)
