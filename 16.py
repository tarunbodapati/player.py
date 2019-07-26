x=int(input())
z=list(map(int,input().split()))
count=0
n={}
for i in range(0,x):
  for j in range(1,x):
     if(z[i]==z[j]):
       count+=1
  n[count]=z[i]
  count=0
y=min(n.keys())
print(n[y])

