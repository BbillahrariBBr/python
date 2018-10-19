def mul_table(number =1):
    m =1
    while m<=10:
        print(number," x ", m, "= ", number*m)
        m += 1


n = input ("please enter a positive number")
if n == "":
    mul_table()

else:
    n = int (n)
    while n<0:
        print("you enter  negative value")
        n = input ("please enter a positive number")
        n = int (n)
        mul_table(n)




    
    

