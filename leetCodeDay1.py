def countEvenDigitNumbers(nums):    
  evenCount = 0
  for i in range(len(nums)):       
    tempHolder = nums[i] // 10
    currentNumberDigit = 1
    while tempHolder > 0:
      currentNumberDigit += 1
      tempHolder = tempHolder // 10
    if currentNumberDigit % 2 == 0:
      evenCount += 1
  return evenCount
            
exampleList1 = [12,345,2,6,7896]
exampleList2 = [555,901,482,1771]
exampleList3 = [252]

print(countEvenDigitNumbers(exampleList1))

print(countEvenDigitNumbers(exampleList2))

print(countEvenDigitNumbers(exampleList3))
