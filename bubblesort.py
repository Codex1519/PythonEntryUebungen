
# Bubblesort

"""
Schreibe ein Funktion,
der man eine Liste mit
beliebig vielen Zahlen als Werten übergeben kann
und die diese Liste sortiert und zurück gibt.

Benutze hierzu den Bubblesort-Algorithmus.
Bei diesem wird die Liste durchlaufen
und jede Zahl mit der jeweils nachfolgenden Zahl verglichen.
Wenn die nachfolgende Zahl kleiner ist,
werden die Zahlen getauscht.
Die Liste wird solange durchlaufen,
bis bei einem Durchlauf keine Zahlen getauscht werden müssen.
"""

feld = [5,6,4,7,1,2,8,9,10]

while True:
    vertauscht = False
    for i in range(len(feld)-1):
        if feld[i] > feld[i+1]:
            temp = feld[i]
            feld[i] = feld[i+1]
            feld[i+1] = temp
            vertauscht = True
    if vertauscht == False: break
    
print("Die Liste wurde mit 'Bubble Sort' sortiert: ",feld)


