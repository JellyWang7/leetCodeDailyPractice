def removeElement(nums, val):
    while True:
        try:
          nums.remove(val)
        except:
          break
    print(nums)

nums = [3,2,2,3]
val = 3
removeElement(nums,val)

nums2 = [0,1,2,2,3,0,4,2]
val2 = 2
removeElement(nums2,val2)

nums1 = [2,2,3]
val1 = 2
removeElement(nums1,val1)