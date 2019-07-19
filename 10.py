    
k,j=list(map(str,input().split(" ")))
z=len(k)
count=0
for i in range(0,z):
  if(k[i]!=j[i]):
       count+=1
if(count==1):
  print("yes")
else:
  print("no")    

