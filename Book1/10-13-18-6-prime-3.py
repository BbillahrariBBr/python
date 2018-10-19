def is_prime3(n):
    if n==2:
        return True # 2 is prime
    if n%2 ==0:
        print(n, " is divisable by 2")
        return False
    if n<2:
        return False
    prime = True
    m = n//2+1
   # print("m is ",m)
    for x in range(3, m,2):
        if n%x == 0:
            print(n, "is divisable by: ",x)
            prime = False
            return prime
    return prime

while True:

    number = input("Please enter a number enter  (0 for exit):")
    number = int(number)
    if number == 0:
        break
    
    prime = is_prime3(number)
    if prime is True:
        print(number, " is prime number")

    else:
        print(number, " is not a prime")
