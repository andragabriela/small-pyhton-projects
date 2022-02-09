n=eval(input("Introduceti un numar: "))
p=1
d=2
while d<=n/2:
    if n%d==0: p=p*d
    d=d+1
print(p)
    
