a = 5
wort = f'abc {a}'

if wort.find('b') > 0:
    pass

if 'b' in wort:
    pass

wort = wort.replace('b', 'BBB')

print(wort[0])

#key  - value 

fahrzeuge = {
    "M-AB-123": "BMW X3",
    "HH-XY-22" : "Audi A3"
}

fahrzeuge['N-AB-123'] = "Opel Corsa"

if "HH-XY-22" in fahrzeuge:
    print(fahrzeuge['HH-XY-22'])

for key, value in fahrzeuge.items():
    print(key, end="\ t")
    print(value)

print("Keys: ")
for key in fahrzeuge.keys():
    print(key)
