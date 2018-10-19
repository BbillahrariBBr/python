import random

number = random.randint(1,1000)
attempts =0
low =1
high=1000

while True:
    print("Guess the Number (between 1 to 1000): ")
    input_number = (low+high)//2
    print("My guess is ", input_number)
    attempts += 1

    if input_number == number:
        print("Yes, ur guess is correct!")
        break
    if input_number> number:
        print("incorrect! please try to guess a smaller number.")
        high = input_number-1
    else:
        print("Incorrect! please Try to guess a larger number")
        low = input_number+1

print("You tried ", attempts, "times to find the correct number.")
