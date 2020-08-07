def mergeSorted(nums1,nums2,m,n):
    lastInNum1 = m - 1
    lastInNum2 = n - 1
    while lastInNum1 >= 0 and lastInNum2 >= 0:
        if nums1[lastInNum1] > nums2[lastInNum2]:
           nums1[lastInNum1+lastInNum2+1] = nums1[lastInNum1]
           lastInNum1 -= 1
        else:
            nums1[lastInNum1+lastInNum2+1] = nums2[lastInNum2]
            lastInNum2 -= 1
    nums1[:lastInNum2+1] = nums2[:lastInNum2+1]
    print(nums1)
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
mergeSorted(nums1, nums2, m, n)
