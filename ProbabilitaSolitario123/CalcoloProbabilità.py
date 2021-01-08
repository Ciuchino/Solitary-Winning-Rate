from random import *
NUMBER_OF_MATCHES = 10000000

print("Loading...")
Mazzo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
NumeroVittorie = 0
for partite in range(0, NUMBER_OF_MATCHES + 1):
    Cont = 1
    Vittoria = True
    shuffle(Mazzo)
    for i in Mazzo:
        # print(i)
        Carta = i
        if Cont == 4:
            Cont = 1
        if (Carta == Cont):
            Vittoria = False
            break
        Cont = Cont + 1
    # print(Mazzo)
    if Vittoria == True:
        NumeroVittorie = NumeroVittorie + 1
    # else:
    #   print("Hai perso!!\n")
    # print(Cont)
    # print(Mazzo)
print("Matches= ")
print("Number of victories ")
print(partite)
print(NumeroVittorie)
print("Victory rate= ")
print(float(NumeroVittorie/partite)*100 )



