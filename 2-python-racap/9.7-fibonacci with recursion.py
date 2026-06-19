def fibonacci(t):

    if t == 0:
        return 0
    elif t == 1:
        return 1
    
    return fibonacci(t - 1) + fibonacci(t - 2)

step = int(input("What step should we calculate? "))
print(fibonacci(step))