number = input("Enter a integer number: ")
number = int(number)

if number <0 :
    print("number is negative")
elif number ==0:
    print("0 is even")
else:
    res= number%2
    if res== 0:
        print(number, " is even")
    else:
        print(number, " is odd")
    
