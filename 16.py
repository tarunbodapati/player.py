x=int(input())
z=[]
count=0
for i in range(0,x):
  z.append(input().split())
m=len(z)  
for i in range(0,x-1):
  for j in range(1,x):  
    if(z[i]!=z[j]):
         count+=1
  if(count==z-1):
    print(z[i])
