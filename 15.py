x=str(input())
x=list(x)
n=len(x)
r={}
count=0
for i in range(0,n-1):
   for j in range(1,n):
       if(x[i]==x[j]):
         count+=1
   r[count]=x[i]
   count=0
z=max(r.keys())
print(r[z])
