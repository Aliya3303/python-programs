n=int(input())
for i in range(n):
    for j in range(n):
        if(i==n//2)or (j==n-1)or(i<=n//2)and (j==0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    else:
        print()
