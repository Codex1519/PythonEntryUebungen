from pathlib import Path
import os

with open('datei.txt', mode='w', encoding="utf-8") as d:
    d.write("#1Dies ist ein Test\n")
    d.write("!!#2Dies ist ein Test\n")
    d.write("#3Dies ist ein Test\n")
    

if Path('datei.txt').exists():
    counter = 0
    with open('datei.txt') as d:
        for zeile in d:
            if not zeile.startswith('!'):
                counter +=1
    print(counter)
    
path = os.path.join("C:\\Benutzer", "Dokumente", "super.txt")
print(path)


with open('datei.txt', mode='w', encoding="utf-8") as d:
    pass
