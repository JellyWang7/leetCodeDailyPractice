def checkIfExist(arr):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i] != arr[j]:
        if arr[i] == 2 * arr[j]:
          return True
        elif arr[j] % 2 == 0 and arr[i] == arr[j] /2:
          return True
      elif arr[i] == arr[j] == 0:
        return True
  return False

arr = [10,2,5,3]
x = checkIfExist(arr)
print(x)

arr1 = [7,1,14,11]
x = checkIfExist(arr1)
print(x)

arr2 = [3,1,7,11]
x = checkIfExist(arr2)
print(x)

arr3 = [0,0]
x = checkIfExist(arr3)
print(x)

