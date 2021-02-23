numbers = [10,3, 5, 1, 2, 91, 3]

def find_farthest_values(numbers):
    min = numbers[0]
    max = numbers[0]
    for i in numbers:
        if i < min:
            min = i
        if i > max:
            max = i
    return (min,max)
    
 

def selectionSort(numList , i, n):
    min = i
    for j in range(i + 1, n):
 
        if numList[j] < numList[min]:
            min = j 
 
    temp = numList[min]
    numList[min] = numList[i]
    numList[i] = temp
 
    if i + 1 < n:
        selectionSort(numList, i + 1, n)
    else:
        print(numList)

numList = [3, 5, 8, 4, 1, 9, -2]

selectionSort(numList, 0, len(numList))

      