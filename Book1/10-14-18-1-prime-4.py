import math

def is_prime4(n):
    if n<2:
        return False
    
    if n==2:
        return True # 2 is prime
    
    if n%2 ==0:
        print(n, "is divisable by 2")
        return False

    m = math.sqrt(n)
    #print ("using sqrt m is: ",m)
    m = int(m)+1
    #print("m+1 is : ",m)
    for x in range(3,m,2):
        if n%x == 0:
            print(n, "is divisable by: ",x)
            return False

    return True


while True:

    number = input("Please enter a number enter  (0 for exit):")
    number = int(number)
    if number == 0:
        break
    
    prime = is_prime4(number)
    if prime is True:
        print(number, " is prime number")

    else:
        print(number, " is not a prime")

    
    
