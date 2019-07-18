y=list(input())
for i in range(0,len(x),2):
    c=y[i]
    y[i]=y[i+1]
    y[i+1]=c
for i in y:
    print(i,end="")
    
