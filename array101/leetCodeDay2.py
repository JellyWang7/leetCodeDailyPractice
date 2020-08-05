import math
def sortedSquares(A):
  resultArray = A
  for i in range(len(A)):
    resultArray[i] = resultArray[i] * resultArray[i]
  resultArray = sorted(resultArray)
  return resultArray
           
exampleList1 = [-4,-1,0,3,10]
exampleList2 = [-7,-3,2,3,11]

print(sortedSquares(exampleList1))

print(sortedSquares(exampleList2))