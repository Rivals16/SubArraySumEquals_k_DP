#! /usr/bin/python3
import time
def mergesort(arr,left,right):
    if(left >= right):
        return
    else:
        mid = (left + right)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)


def merge(arr,left,mid,right):
    l = []
    r = []
    for i in range(left,mid+1):
        l.append(arr[i])
    for i in range(mid+1,right+1):
        r.append(arr[i])
    index = left

    i = 0 ; j = 0
    while(i!=len(l) and j !=len(r)):
        if(l[i]<r[j]):
            arr[index] = l[i]
            i+=1
        else:
            arr[index] = r[j]
            j+=1
        index +=1
    if(i == len(l) and j != len(r)):
        for x in range(j,len(r)):
            arr[index] = r[x]
            index+=1
    if(j == len(r) and i != len(l)):
        for x in range(i,len(l)):
            arr[index] = l[x]
            index += 1


ls = [int(x) for x in input().split()]
ar = []
ar = ls
start = time.process_time()
mergesort(ls,0,len(ls)-1)
print(ls)
print(time.process_time()-start)
start2 = time.process_time()
ar.sort()
print(time.process_time()-start2)
