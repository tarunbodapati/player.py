x,y=list(map(str,input().split(" ")))
z=len(x)
n=len(y)
count=0
n=0
for i in range(z-1):
  if(x[i]==x[i+1]):
     count+=1
     if(count==1):
         break
for i in range(n-1):
  if(y[i]==y[i+1]):
     n+=1
     if(count==1):
       break
if(count==n):
  print("no")
else:  
  print("yes")
