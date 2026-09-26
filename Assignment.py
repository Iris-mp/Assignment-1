# Welcome to my first assignment's program!
# -------------------------------------------------------
# Assignment 1
# Written by Iris-Maria Palade (2540435)
# For “Programming in Science” Section 00004 – Fall 2026
# --------------------------------------------------------

# Begining of the program
# #Question 1: Electricity Cost Calculator
# This program uses the data entered by the user (power amount, time, and electrical rate) to calculate and return to the user the cost of electricity and classifies it by comparing it to a set cost.

power = int(input("Enter the power in watts:"))
time = int(input("Enter the number of hours:"))
rate = float(input("Enter the electricity rate per kWh:")) #For lines 10,11,12, the user is prompted to type in the data needed (the power used, the time it was used for and the electrical rate) using their keyboards.


def calculate_cost(power, time, rate):
    energy_cost = round((((power * time) / 1000) * rate), 2) #Here, the formula to calculte the cost of electricity is written, and the fucntion round is used to round the result to 2 decimal points.
    return energy_cost 
    #In the lines 15 to 17, a function is defined to calculate the cost of electrivity depending on the amount of power used in a period of time and the electricity rate.


energy_cost = calculate_cost(power, time, rate)
print("Electricity cost:", calculate_cost(power, time, rate), "$") #Here, the variable "energy_cost" is defined and the result of the electrical cost is displayed to the user using the print function. 

if energy_cost < 1:
    print("Cost category: Low cost")
elif energy_cost > 1 and energy_cost < 5:
    print("Cost category: Moderate cost")
else:
    print("Cost category: High cost")
# In the lines 24 through 29, the if/elif/else function is used to classify the cost as low, moderate or high depending of it's ammount by comparing it to a set cost and it returns the classification to the user following the cost of electricity.

# --------------------------------------------------------
# Question 2: Final Grade Calculator
# This program uses the data entered by the user (lab, midterm and final exam grades) to calculate and return to the user their final grade in that class taking into account each section's ponderation and classifies it by comparing it to a set grade.

lab_grade = int(input("Enter the lab grade:"))
midterm_grade = int(input("Enter the midterm exam grade:"))
final_exam_grade = int(input("Enter the final exam grade:")) #For lines 32,33,34, the user is prompted to type in the data needed (their grades) using their keyboards.


def calculate_grade(lab_grade, midterm_grade, final_grade):
    final_grade = round((lab_grade * 0.30) + (midterm_grade * 0.30) + (final_grade * 0.40), 1)
    return final_grade
#In the lines 40 to 42, a functuion is defined to calculate the final grade of a student, taking into account the grades they have entered into the program as well as their respective ponderation. 

final_grade = calculate_grade(lab_grade, midterm_grade, final_exam_grade)
print("Final grade:", final_grade) #Here, the variable "final_grade" is defined and the student's final grade for that class is returned and displayed to them using the print function. 

if final_grade >= 90:
    print("Result: Excellent")
elif final_grade >= 80 and final_grade < 90:
    print("Result: Very Good")
elif final_grade >= 70 and final_grade < 80:
    print("Result: Good")
elif final_grade >= 60 and final_grade < 70:
    print("Result: Satisfactory")
else:
    print("Result: Needs Improvement")
# In the lines 48 through 57, the if/elif/else function is used to classify the student's grade as excellent, very good, good, satisfactory or as needs improvement by comparing it to a set grade and it returns the classification to the user following their final grade.   
# -------------------------------------------------------
# End of the program
