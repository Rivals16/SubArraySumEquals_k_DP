#! /usr/bin/python3
print('Total Testcases:',end='')
for __ in range(int(input())):
    print('Enter Value Of Size And Sum To Find : ',end =' ')
    n , sum = map(int,input().split())
    ar = []
    print('Enter Value Of The Elements : ')
    for i in range(n):
        ar.append(int(input()))
    n = len(ar)
    ls = [[0]*(sum+1) for _ in range (n)]
    for i in range (n):
        ls[i][0] = 1
    for i in range(n):
        for j in range(1,sum+1):
            if(i==0):
                if(ar[i] == j):
                    ls[i][j] = 1
                else:
                    ls[i][j] = 0
            else:
                if(ls[i-1][j]==1):
                    ls[i][j] = 1
                elif(j<ar[i]):
                    ls[i][j] = 0
                else:
                    if(ls[i-1][j-ar[i]]==1):
                        ls[i][j] = 1
                    else:
                        ls[i][j] = 0
    if(ls[n-1][sum]==1):
        print('Present')
    else:
        print('Not Present')
