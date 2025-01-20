# Zahlenreihen

# 1. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5

def schleife1():
    for i in range(1, 6):
        print(i, end=" ")
    print()
        
schleife1()        

# 2. Schreibe eine Schleife, die Folgendes ausgibt:
# 100 90 80 70 60 50 40 30 20 10

def schleife2():
    for i in range(100, 0, -10):
        print(i, end=" ")
    print()
    
schleife2()

# 3. Schreibe eine Schleife, die Folgendes ausgibt:
# 2000 3000 4000 5000 6000

def schleife3():
    for i in range(2000, 7000, 1000):
            print(i, end=" ")
    print()
    
schleife3()

# 4. Schreibe eine Schleife, die Folgendes ausgibt:
# 2.0 1.5 1.0 0.5 0.0 -0.5 -1.0

def schleife4():
    for i in range(4, -3, -1):
        print(i/2, end=" ")
    print()
    
schleife4()

# 5. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 25 29

def schleife5():
    for i in range(13, 30, 4):
        print(i, end=" ")
    print()

schleife5()

# 6. Schreibe eine Schleife, die Folgendes ausgibt:
# 1.0 2.2 3.4 4.6 5.8 7.0 8.2 9.4

def schleife6():
    i = 1.0
    while i < 10.0:
        print(f"{i:.1f}", end=" ")
        i += 1.2
    print()
    
schleife6()

# 7. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 6 8 9 10

def schleife7():
    for i in range(1, 11):
        if i == 7:
            continue
        print(i, end=" ")
    print()
    
schleife7()

# 8. Schreibe eine Schleife, die Folgendes ausgibt:
# 13 17 21 29 33 37 45

def schleife8():
    for i in range(13, 46, 4):
        if i == 25:
            continue
        print(i, end=" ")
    print()
    
schleife8()

# 9. Schreibe eine Schleife, die Folgendes ausgibt:
# Z5 Z7 Z9 Z11 Z13

def schleife9():
    for i in range(5, 15, 2):
        print(f"Z{i}", end=" ")#
    print()

schleife9()

# 10. Schreibe eine Schleife, die Folgendes ausgibt:
# a2b3 a12b13 a22b23

def schleife10():
    for i in range(2, 24, 10):
        print(f"a{i}b{i+1}", end=" ")
    print()

schleife10()

# 11. Schreibe eine Schleife,
# die alle Zahlen von 1 bis 20 addiert
# und danach das Endergebnis ausgibt.

def schleife11():
    summe = 0
    for i in range(1, 21):
        summe += i
    print(summe)

schleife11()

# 12. Schreibe eine Schleife, die Folgendes ausgibt:
# 1 2 3 4 5 4 3 2 1

def schleife12():
    for i in range(1, 6):
        print(i, end=" ")
    for i in range(4, 0, -1):
        print(i, end=" ")
    print()
    
schleife12()
