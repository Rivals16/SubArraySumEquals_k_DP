#! /bin/python3
def quicksort(unsortedArray,left,right):
    if(left>=right):
        return
    else:
        pivot = unsortedArray[(left + right)// 2]
        index = partition(unsortedArray,left,right,pivot)
        quicksort(unsortedArray,left,index-1)
        quicksort(unsortedArray,index,right)

def partition(unsortedArray,left,right,pivot):
    while(left <= right):
        while(unsortedArray[left] < pivot  ):
            left += 1
        while(unsortedArray[right] > pivot ):
            right -= 1
        if(left <= right):
            unsortedArray[left],unsortedArray[right] = unsortedArray[right],unsortedArray[left]
            left += 1
            right -= 1
    return left

unsortedArray=[14,1,3,9,2,6,7,8,9,2,4,6]
quicksort(unsortedArray,0,len(unsortedArray)-1)
print(unsortedArray)
