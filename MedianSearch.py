def medfind(ar,left,right,median):
    if(len(ar)<right):
        if(len(ar)!=left):
            x = ar[left:len(ar)]
            x.sort()
            
            median.append(x[len(x)//2])
        return
    else:
        x = ar[left:right]
        x.sort()
        median.append(x[len(x)//2])
        medfind(ar,right,right+5,median)
    
ar = [25,21,98,100,76,22,43,60,89,87,83,84]
median = []
medfind(ar,0,5,median)
median.sort()
pivot = median[len(median)//2]
median.clear()
median = [0]*len(ar)
start = 0 
for i in ar:
    if(i<pivot):
        median[start] = i
        start+=1
median[start] = pivot
start +=1
for i in ar:
    if(i>pivot):
        median[start] = i
        start+=1
print(*median)
index = median.index(pivot)
k = int(input())
if(k <=len(ar) ):
    if(k-1==index):
        print(median[index])
    elif(k<=index):
        x = median[0:index]
        x.sort()
        print(x[k-1])
    else:
        x = median[index+1:len(ar)]
        x.sort()
        print(x[k-index-2])
