year = input("Enter year yyyy: ")
year = int(year)

if year %100 !=0 and year % 4 ==0:
    print(year," yes")
elif year %100 == 0 and year % 400 == 0:
    print (year," yes")
else :
    print("no")
