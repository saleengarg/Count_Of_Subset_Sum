def subsetsum(arr,n,s):
    rows,cols=n+1,s+1
    a = [[0 for i in range(cols)] for j in range(rows)] 
    for i in range(n+1):
        for j in  range(s+1):
            if i==0:
                a[i][j]=0
            if j==0:
                a[i][j]=1
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                a[i][j]=a[i-1][j-arr[i-1]]+a[i-1][j]
            else:
                a[i][j]=a[i-1][j]
    return a[n][s]
                
                
                
             
r=subsetsum([2,3,7,8,10],5,10)
print(r)
##Output
3  