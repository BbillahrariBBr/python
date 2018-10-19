marks = input("plz enter your Matks: ")
marks = int(marks)
grade_list = ["A+", "A","A-","B","F",]
if marks<0 :
    print("you enter Negative number")
elif marks>100:
    print("You enter a number which is larger thn 100")
else:
    if marks >= 80:
        grade = grade_list[0]
    elif marks >=70:
        grade = grade_list[1]
    elif marks >=60:
        grade = grade_list[2]
    elif marks >=50:
        grade = grade_list[3]
    else:
        grade = grade_list[4]
    print ("your Grade is: " , grade)
    
