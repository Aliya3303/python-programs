n=int(input())
for i in range(n):
    for j in range(n):
        if(j+i==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    else:
        print()
