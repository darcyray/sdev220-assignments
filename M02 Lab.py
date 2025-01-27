''' 
Darcy Ralstin - Module 2 Lab
This program will accept students' first and last names & gpa as input. 
It will then process the input. 
If the gpa is 3.5 or higher, it will print a 'Dean's List' message. 
If the gpa is 3.25 or higher, it will print an ' Honor Role' message.
'''

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name. Enter 'ZZZ' to quit: ")
gpa = float(input("Please enter your grade point average: "))

while last_name != "ZZZ":
    if gpa >= 3.5:
        print("Congratulations, you have made the Dean's List!")
        break
    elif gpa >= 3.25:
        print("Congratulations, you have made the Honor Roll!")
        break
    elif gpa < 3.25:
        print("Your gpa is not high enough to qualify for the Honor Roll or Dean's List.")
        break
else:
    exit
    
    
