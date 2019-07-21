m,n=list(map(int,input().split()))
x=list(map(int,input().split()))
for s in range(0,n):
  x=([x[-1]] + x[:-1])
print(*x)
