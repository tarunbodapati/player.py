z,l=map(int,input().split())
count=0
for m in range(z,l+1):
    if m>1:
        for n in range(2,m):
            if(m%n==0):
                break
        else:
            count=count+1
print(count)
