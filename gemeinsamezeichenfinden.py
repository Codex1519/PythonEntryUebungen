
# Gemeinsame Zeichen finden

# Schreibe ein Programm, dass ermittelt,
# welches die gemeinsamen Buchstaben der Wörter
# "Python" und "Programmierung" sind?

def gemeinsameszeichen(wort1, wort2):
    gemeinsam = []
    for zeichen in wort1:
        if zeichen in wort2:
            gemeinsam.append(zeichen)
    return gemeinsam

print(gemeinsameszeichen("Python", "Programmierung"))