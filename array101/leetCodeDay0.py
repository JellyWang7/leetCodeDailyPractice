def findMaxConsecutiveOnes(nums):
      count = nums.count(1)
      if count == len(nums):
        return count
      elif count == 0:
        return 0
      else:
        count = 0
        result = 1
        for i in range(len(nums)):       
            if nums[i] == 0:
                count = 0
            else:
                count += 1
                result = max(count,result)
        return result
            
exampleList = [1,1,0,1,1,1]

print(findMaxConsecutiveOnes(exampleList))



