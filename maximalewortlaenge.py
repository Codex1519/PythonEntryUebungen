
# Maximale Wortlänge

# Ermittel die maximale Wortlänge in der folgenden Zeichenkette
# auf mindestens zwei verschiedene Arten:

s = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor"
s += " invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et"
s += " accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata"
s += " sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing"
s += " elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat,"
s += " sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd"
s += " gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."



zeichenkettenlänge = len(s)
print("Mit der Methode len() ermittelte Wortlänge: ",zeichenkettenlänge)

zeichenkettenlänge = 0

for char in s:
    zeichenkettenlänge += 1
    
print("Mit iterativen Methode ermittelte Wortlängen: ",zeichenkettenlänge)