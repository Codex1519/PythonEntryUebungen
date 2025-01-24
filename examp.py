number = 10
for n in range(2, int(number**0.5)+1):
    if n % number == 0:
        print(n)

print(number)