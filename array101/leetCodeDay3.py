def duplicateZeros(arr):
    expandArrayBy = 0
    sizeOfArray = len(arr) - 1
    for i in range(sizeOfArray + 1):
        if i > sizeOfArray - expandArrayBy:
            break
        if arr[i] == 0:
            if i == sizeOfArray - expandArrayBy:
                arr[sizeOfArray] = 0
                sizeOfArray -= 1
                break
            expandArrayBy += 1
    lastNum = sizeOfArray - expandArrayBy
    for j in range(lastNum, -1, -1):
        if arr[j] == 0:
            arr[j + expandArrayBy] = 0
            expandArrayBy -= 1
            arr[j + expandArrayBy] = 0
        else:
            arr[j + expandArrayBy] = arr[j]


arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)
print(arr)

arr1 = [1,2,3]
duplicateZeros(arr1)
print(arr1)