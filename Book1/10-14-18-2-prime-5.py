import math

def is_prime4(n=1013):
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


def is_prime3(n=1013):
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


import timeit
t1 = timeit.timeit(is_prime3)
t2 = timeit.timeit(is_prime4)
print("t1, prime3 : ",t1, "t2, prime4 : ",t2, t1/t2)


