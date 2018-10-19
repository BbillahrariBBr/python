'''def add_numbers(numbers):
    result = 0
    for numbers in numbers:
        result += numbers
    return result
result = add_numbers([1,2,30,4,5,9])
print(result)


def test_fnc(li):
    li[0] = 10

my_list = [1,2,3,4,5]
print("before function call ", my_list)
test_fnc(my_list)
print("after cunction call " ,my_list)
'''

def avg_fnc(numbers):
    result = 0
    counter =0
    for numbers in numbers:
        result += numbers
        counter +=1
    return result/counter

result = avg_fnc([5,3])
print(result)
        
