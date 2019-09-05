#! /usr/bin/python3
import time
def countingSort(insertedArray,countArray,sortedArray):

    for i in range(len(insertedArray)):
        countArray[insertedArray[i]] += 1
    print("Counting Array Is : ",countArray)
    for i in range(1,len(countArray)):
        countArray[i]+=countArray[i-1]
    print("Modified Counting Array : ",countArray)
    for i in range(0,len(insertedArray),1):
        sortedArray[countArray[insertedArray[i]]-1] = insertedArray[i]
        countArray[insertedArray[i]]-=1
    return sortedArray
if __name__ == "__main__":
    insertedArray = list(map(int,input('Enter Numbers Counting Sort : ').split()))
    maximumElement = max(insertedArray)
    countArray = [0]*(maximumElement+1)
    sortedArray = [0]*len(insertedArray)
    start = time.process_time()
    print("Sorted Array Is:",countingSort(insertedArray,countArray,sortedArray))
    print("Time Taken By Counting Sort : ",time.process_time()-start)
    start = time.process_time()
    insertedArray.sort()
    print(insertedArray)
    print("Time Taken By Tim Sort : ",time.process_time()-start)
