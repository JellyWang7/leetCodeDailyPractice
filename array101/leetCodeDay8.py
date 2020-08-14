def validMountainArray(arr):
  N = len(arr)
  i = 0
  while i + 1 < N and arr[i] < arr[i+1]:
        i += 1
  if i == 0 or i == N-1:
        return False
  while i + 1 < N and arr[i] > arr [i+1]:
        i += 1
  return i == N-1



arr = [2,1]
x = validMountainArray(arr)
print(x)

arr1 = [3,5,5]
x = validMountainArray(arr1)
print(x)

arr2 = [0,3,2,1]
x = validMountainArray(arr2)
print(x)
