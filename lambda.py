# def is_even(a):
#     # lambda a: 
#     return a % 2 == 0

zahlen = [1, 2, 3, 4]

# gefilterte_zahlen = list(filter(lambda a: a % 2 == 0, zahlen))

# print(gefilterte_zahlen)

# def addone(a):
#     return a+1

mapped_zahlen = list(map(lambda a:a+1, zahlen))
print(mapped_zahlen)