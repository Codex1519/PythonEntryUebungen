
# Vokale suchen

# Extrahiere aus der Zeichenkette "Hello World!" alle Vokale
# und verbinde diese zu einer neuen Zeichenkette.
# Löse es einmal per Higher-Order-Funktion und einmal klassisch.

# Klassische Lösung
text = "Hello World!"
vokale = "aeiouAEIOU"
ausgabe = ""

for char in text:
    if char in vokale:
        ausgabe += char
        
print(ausgabe)


text = "Hello World!"
vokale = "aeiouAEIOU"

ausgabe = "".join(filter(lambda char: char in vokale, text))
print(ausgabe)

