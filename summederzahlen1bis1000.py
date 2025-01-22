from functools import reduce


# Summe der Zahlen von 1 bis 1000

# Erarbeite mindestens vier Arten, die Summe der Zahlen von 1 bis 1000 zu berechnen:
# Z.B. for, while, reduce() mit lambda und Liste, sum() mit Generator Expression

summe = 0
for i in range(1, 1001):
    summe += i
print(summe)    

result1 = 0
i = 1 
while i <= 1000:
    result1 += i
    i  += 1
print(result1)


result2 = sum(range(1, 1001))
print(result2)


result3 = reduce(lambda x, y: x + y, range(1, 1001))
print(result3)

