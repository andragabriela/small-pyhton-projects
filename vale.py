#candidat, multimea solutie, daca un candidat partial poate conduce la o lista solutie, spatiu de cautare
#candidat toate listele de lungimea variata x= (x0, x1,. .. , xi), xi∈(0,1,.. ,N− 1)
#multime solutie daca xi!=xj si au aspect de vale (pana la un anumit element scad si dupa cresc)
#dimendiunea spatiu de cautare in cazul de fata e 5 la n
#spatiu de cautare sunt solutile candidat
def print_sol(lista, array):
    for i in range(len(lista)):
        print(array[lista[i]], end=' ')
    print()

def valid(lista):
    #conditie permutari
    for i in range(len(lista)-1):
        if lista[-1]==lista[i]:
            return False
    return True

def solutie(lista, n):
    '''
    Verifica daca lista are aspect de vale
    :param lista:
    :return:
    '''
    if len(lista)!=n:
        return False

    if lista[0]<lista[1]:
        return False

    descr=True
    i=0
    while i<len(lista)-1 and descr==True:
        if lista[i]<lista[i+1]:
            descr=False
        else: i+=1

#daca e bine aici desc va fi false
    asc=True
    while i<len(lista)-1 and asc==True:
        if lista[i]>lista[i+1]:
            asc=False
        else: i+=1
    if descr==False and asc==True:
        return True
    else: return False



def back(lista, array):
    lista.append(0)
    for i in range(len(array)):
        lista[-1]=i
        if valid(lista):
            if solutie(lista, len(array)):
                print_sol(lista, array)
            back(lista, array)
    lista.pop()

def back_it(lista, array):
    lista.append(-1)
    while len(lista) > 0:
        choosed = False
        while not choosed and lista[-1] < len(array) - 1:
            lista[-1] = lista[-1] + 1  # increase the last component
            choosed = valid(lista)
        if choosed:
            if solutie(lista, len(array)):
                print_sol(lista, array)
            lista.append(-1)  # expand candidate solution
        else:
            lista = lista[:-1]

array=[1,2,3,4,5]
back([], array)

back_it([],array)




def test_valid():
    a=[1,0,3]
    assert solutie(a,3)==True

    a=[4,3,0,1,2]
    assert solutie(a,5)==True






test_valid()

