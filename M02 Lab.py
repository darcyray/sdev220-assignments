''' 
Darcy Ralstin - Module 2 Lab
This program will accept students' first and last names & gpa as input. 
It will then process the input. 
If the gpa is 3.5 or higher, it will print a 'Dean's List' message. 
If the gpa is 3.25 or higher, it will print an ' Honor Role' message.
'''

# Constants
DEANS_LIST: float = 3.5
HONOR_ROLL: float = 3.25
SENTINEL: str = "ZZZ"


# Variables
first_name: str = ''
last_name: str = ''
gpa: float = 0.0

# Main
while last_name != SENTINEL:
    last_name = input("Please enter your last name. Enter ZZZ to quit: ")
    if last_name == SENTINEL:
        break
    first_name = input("Please enter your first name: ")
    gpa = input("Please enter your GPA: ")
    
    try:
        gpa = float(gpa)
    except ValueError:
        continue
    if gpa >= DEANS_LIST:
        print(f"Congratulations, {first_name}  {last_name}, you have made the Dean's List.")
    elif gpa >= HONOR_ROLL:
        print(f"Congratulations, {first_name}  {last_name}, you have made the Honor Roll!")
exit
    
    
