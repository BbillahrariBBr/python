def div (a,b):
    try:
        return a/b
    except ZeroDivisionError: 
        print("Can not divide by Zero")
    except TypeError:
        print("Unsupported type. did you use string?")
       
print(div(10,2))
print(div(3,0))
print(div(9,3))
print(div("12",3))
