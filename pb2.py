num=eval(input("Introduceti un numar: "))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"nu este prim")
            print(i,"de",num//i,"este",num)
            break
        else:
            print(num, "este prim")
else:
    print(num,"nu este numar prim")
