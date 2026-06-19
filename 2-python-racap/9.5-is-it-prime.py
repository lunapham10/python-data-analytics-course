checkingnumber = int(input("Give a number: "))

is_prime = True

if checkingnumber <=1:
    is_prime = False;
else:
    for i in range (2, checkingnumber):
        if checkingnumber % i == 0:
            is_prime = False
            break  
        
if is_prime == True:
    print (f"{checkingnumber} is a prime number")
else:            
    print (f"{checkingnumber} is not a prime number")