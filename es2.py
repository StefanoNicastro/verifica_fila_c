#es2

## **Esercizio 2**:
#Supponiamo di avere una tupla contenente i dati di consumo energetico mensile di diverse abitazioni in diverse città. Ogni voce nella tupla è strutturata nel seguente modo:


tupla_consumi_energetici = (
    ("Milano", [
        ("gennaio", ("elettrico", 300)),
        ("gennaio", ("gas", 150)),
        ("febbraio", ("elettrico", 280)),
        ("febbraio", ("gas", 120)),
        ("marzo", ("elettrico" ,400)),
        ("marzo", ("gas", 200)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Brescia", [
        ("gennaio", ("elettrico", 280)),
        ("gennaio", ("gas", 140)),
        ("febbraio", ("elettrico", 260)),
        ("febbraio", ("gas", 130)),
        ("marzo", ("elettrico",320)),
        ("marzo", ("gas",240)),
        # Aggiungi altri mesi e consumi
    ]),
    ("Catania", [
        ("gennaio", ("elettrico", 120)),
        ("gennaio", ("gas", 200)),
        ("febbraio", ("elettrico", 460)),
        ("febbraio", ("gas", 137)),
        ("marzo", ("elettrico",620)),
        ("marzo", ("gas",500)),
        # Aggiungi altri mesi e consumi
    ])
)

"""Definisci una funzione analizza_consumi_energetici che
riceva come parametro il nome della città e il nome della risorsa energetica e restituisca una tupla con la seguente struttura:
```python
(media_risorsa, (max_risorsa, meseMax_risorsa))
```

Dove:
- `media_risorsa` è il consumo medio della risorsa.
- `max_risorsa` è il valore massimo di consumo della risorsa.
- `mese_max_risorsa` è il mese in cui si è verificata il consumo massimo per quella risorsa.

Aggiungi alla tupla altre citta e mesi.

Assicurati di gestire correttamente i casi in cui il nome della citta o della risorsa forniti come parametro non siano presenti nella tupla dei dati.
"""

def analizza_consumi_energetici(città, mese, consumo):
    cons_el=[]

    cont=0
    media_risorsa=0
    for tipoCon, costo in consumo:
        if(tipoCon=="elettrico"):
            media+=costo
            cont+=1
            cons_el.append(costo)
    
    max_risorsa=max(cons_el)
    media_risorsa/=cont
    return media_risorsa, (max_risorsa)
    



for città, *mese, consumo in tupla_consumi_energetici:
    cons_el=[]
    stampa=analizza_consumi_energetici(città, mese, consumo)
    print(f"Città: {città} mese: {mese} consumi:\n{stampa}")