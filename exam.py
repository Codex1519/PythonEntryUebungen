tels = {'a': 12, 'b': 18}
tels['c'] = 19  # geht

name = "Max Meier"
n = name + "!"  # geht

a =(2,4)
a[0] = 3    # geht nicht

b = (3,)
print(b[0]) # geht 

zahlen =list(range(1,5)) # 1,2,3,4
zahlen[0] = 10 # 10,2,3,4 # geht
zahlen[5] = 5 # nein, out of range

y = 55
liste = [1, "x",y]
print(liste[0] +liste[2])