#es1
#Immagina di gestire i risultati di un torneo sportivo attraverso una tupla contenente le informazioni sulle partite. 
#Ogni voce della tupla rappresenta una partita e contiene le seguenti informazioni: squadra di casa, squadra ospite, punteggio della squadra di casa, punteggio della squadra ospite.

tupla_partite = (
    ("SquadraA", "SquadraB", 3, 2),
    ("SquadraC", "SquadraD", 1, 1),
    ("SquadraB", "SquadraC", 2, 4),
    ("SquadraD", "SquadraA", 0, 3),
    ("SquadraB", "SquadraD", 1, 2),
)

"""Definisci le seguenti funzioni utilizzando le funzioni predefinite sum, min, max per le liste:

1. **media_gol_partite(tupla_partite)**: una funzione che accetti come parametro la tupla delle partite e restituisca la media dei gol segnati in tutte le partite.

2. **media_gol_squadra(tupla_partite, squadra)**: una funzione che accetti come parametri la tupla delle partite e il nome di una squadra, e restituisca la media dei gol segnati dalla squadra in tutte le partite in cui ha partecipato.

3. **partita_con_piu_gol(tupla_partite)**: una funzione che restituisca una tupla contenente la partita con il maggior numero di gol segnati e i relativi punteggi.

4. **partita_con_meno_gol(tupla_partite)**: una funzione che restituisca una tupla contenente la partita con il minor numero di gol segnati e i relativi punteggi.

5. **percentuale_vittorie_squadra(tupla_partite, squadra)**: una funzione che restituisca la percentuale di partite vinte dalla squadra rispetto al totale delle partite disputate.

6. Prevedi un menu di scelta che consenta all'utente di selezionare un'operazione tra le opzioni disponibili."""

def media_gol_partite(tupla_partite):
    nPar=0
    media=0
    for (squad1, squad2, golS1, golS2) in tupla_partite:
        nPar+=1
        media+=golS1+golS2
    media/=nPar
    print(f"Media gol di tutte le partite: {media}\n")



def media_gol_squadra(tupla_partite, squad1):                 ##################
    squad_contrG=[]
    cont=0
    nG=0
    if(squad1 not in squad_contrG):
        for (sq1, sq2, golS1, golS2) in tupla_partite:
            if(sq1==squad1):
                if(golS1>0):
                    cont+=1
                    nG+=golS1
                else:
                    cont+=1
            
            if(sq2==squad1):
                if(golS2>0):
                    cont+=1
                    nG+=golS2
                else:
                    cont+=1
    
    nG/=cont
    print(f"Media gol a partita di {squad1}: {nG}")


def partita_con_piu_gol(tupla_partite):
    gol_per_part=[]
    for (squad1, squad2, golS1, golS2) in tupla_partite:
        gol_per_part.append(golS1+golS2)
    
    piùGol=max(gol_per_part)
    print(f"Partita con più gol: {tupla_partite[gol_per_part.index(piùGol)]}\n")



def partita_con_meno_gol(tupla_partite):
    gol_per_part=[]
    for (squad1, squad2, golS1, golS2) in tupla_partite:
        gol_per_part.append(golS1+golS2)
    
    menoGol=min(gol_per_part)
    print(f"Partita con meno gol: {tupla_partite[gol_per_part.index(menoGol)]}\n")



def percentuale_vittorie_squadra(tupla_partite, squad1):
    cont=0
    pVin=0

    if(squad1 not in squad_contr):
        for (sq1, sq2, golS1, golS2) in tupla_partite:
            if(sq1==squad1):
                cont+=1
                if(golS1>golS2):
                    pVin+=1
            if(sq2==squad1):
                cont+=1
                if(golS2>golS1):
                    pVin+=1
    percPVin=(100*pVin/cont)
    squad_contr.append((squad1,percPVin))
    



while True:
    scelta=int(input(("MENU seleziona l'azione da eseguire (da 1 a 5, 0 per uscire )")))
    if(scelta==0):
        break
    elif(scelta==1):
        media_gol_partite(tupla_partite)

    elif(scelta==2):
        squad_contrG=[]
        for (squad1, squad2, golS1, golS2) in tupla_partite:
            media_gol_squadra(tupla_partite, squad1)

    elif(scelta==3):
        partita_con_piu_gol(tupla_partite)

    elif(scelta==4):
        partita_con_meno_gol(tupla_partite)

    elif(scelta==5):
        squad_contr=[]
        for (squad1, squad2, golS1, golS2) in tupla_partite:
            percentuale_vittorie_squadra(tupla_partite, squad1)
        print(squad_contr)
    else:
        print("Opzione non disponibile, reinserisci\n")

print("Programma terminato")