start = 10
while start > 0:
    print(start)
    start = start -1
    
def countdown(n):
    if n < 0:
        return
    print(n)
    countdown(n-1)
    
countdown(10)
    