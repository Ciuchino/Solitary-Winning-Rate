from random import *
NUMBER_OF_MATCHES = 1000000

NumeroVittorie = 0
print("Loading...")
for partite in range(0, NUMBER_OF_MATCHES + 1):
    Vittoria = True
    # Mazzo di carte napoletane. Ogni elemento è un array il cui primo elemento rappresenta il segno,
    # mentre il secondo è il numero.
    Mazzo = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9],
             [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1, 8], [1, 9],
             [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2, 8], [2, 9],
             [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9]]

    shuffle(Mazzo)  # Mischio il mazzo
    # print(Mazzo)
    # Prendo le ultime quattro carte dal mazzo
    Vite = [Mazzo[-4], Mazzo[-3], Mazzo[-2], Mazzo[-1]]
    # print(Vite)
    # Elimino le le quattro vite dal mazzo
    Mazzo.remove(Mazzo[-4])
    Mazzo.remove(Mazzo[-3])
    Mazzo.remove(Mazzo[-2])
    Mazzo.remove(Mazzo[-1])
    # print(Mazzo)

    # Inizio la partita
    for Carta in Vite:
        CartaPescata = Carta
        # print(CartaPescata)
        # Leggo il seme e il numero della carta pescata
        Seme = CartaPescata[0]
        Numero = CartaPescata[1]
        # Se pesco un Re passo alla prossima carta tra le vite
        if Numero == 9:
            continue
        while (Numero != 9):
            # Scambio la carta pescata con la corrispondente carta del mazzo, trovato moltiplicando il seme per il
            # numero di carte con lo stesso seme addizionato al numero della carta.
            Mazzo[Seme * 9 + Numero], CartaPescata = CartaPescata, Mazzo[Seme * 9 + Numero]
            Seme = CartaPescata[0]
            Numero = CartaPescata[1]
            # print(CartaPescata)
    # Continuo finchè non pesco un Re, esco dal ciclo e pesco un'altra carta dalle vite

    # Rimane da fare solamente il controllo, ovvero rivedere tutte le carte fino alla quintultima, se sono tutte in ordine allora la partita è vinta
    Seme = 0
    Numero = 0
     #print(Mazzo)
    for Carta in Mazzo:
        # Controllo il mazzo sia in ordine
        if Carta != [Seme, Numero]:
            Vittoria = False
            #print("Hai perso!")
            # print(Carta)
            # print(Seme)
            # print(Numero)
            break
        Numero = Numero + 1
        # Se arrivo alla posizione del Re Incremento il Seme e porto la carta a 0
        if Numero == 9:
            Seme = Seme + 1
            Numero = 0

    if Vittoria:
        #print("Hai vinto!")
        NumeroVittorie = NumeroVittorie + 1

print("Matches= ")
print("Number of victories ")
print(partite)
print(NumeroVittorie)
print("Victory rate= ")
print(float(NumeroVittorie/partite)*100 )