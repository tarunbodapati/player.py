    
a1=int(input())
x1=str(input())
if (len(x1)<=a1):
    d1=x1.replace("a","")
    e1=d1.replace("A","")
    f1=e1.replace("e","")
    g1=f1.replace("E","")
    h1=g1.replace("i","")
    i1=h1.replace("I","")
    j1=i1.replace("o","")
    k1=j1.replace("O","")
    l1=k1.replace("u","")
    m1=l1.replace("U","")
    c1=m1[::-1]
    print(c1)
