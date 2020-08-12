def removeDuplicates(nums):
  if len(nums) == 0:
    return 0
  compareIndex =  0
  for i in range(len(nums)):
    if nums[i] != nums[compareIndex]:
      compareIndex += 1
      nums[compareIndex] = nums[i]
  nums = nums[:compareIndex+1]
  print(nums)
  return compareIndex + 1

nums = [1,1,2]
removeDuplicates(nums)

nums1 =  [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums1)