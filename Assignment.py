print("Welcome to my first assignment's program!")
#-------------------------------------------------------
#Assignment 1
#Written by Iris-Maria Palade (2540435)
#For “Programming in Science” Section 00004 – Fall 2026
#--------------------------------------------------------

#Begining of the program
#Question 1: Electricity Cost Calculator
#This program uses the data entered by the user (power amount, time, and electrical rate) to calculate and return to the user the cost of electricity and classifies it by comparing it to a set cost.

#In the following lines, the user is prompted to type in the data needed (the power used, the time it was used for and the electrical rate) using their keyboards.
power = float(input("Enter the power in watts:"))
time = float(input("Enter the number of hours:"))
rate = float(input("Enter the electricity rate per kWh:")) 

#In the lines below, a function is defined to calculate the cost of electrivity depending on the amount of power used in a period of time and the electricity rate.
def calculate_cost(power, time, rate):
    energy_cost = round((((power * time) / 1000) * rate), 2) #Here, the formula to calculte the cost of electricity is written, and the fucntion round is used to round the result to 2 decimal points.
    return energy_cost 

#Here, the variable "energy_cost" is defined and the result of the electrical cost is displayed to the user using the print function.
energy_cost = calculate_cost(power, time, rate)
print("Electricity cost: $"+energy_cost)  

# In the lines below, the if/elif/else function is used to classify the cost as low, moderate or high depending of it's ammount by comparing it to a set cost and it returns the classification to the user following the cost of electricity.
if energy_cost < 1:
    print("Cost category: Low cost")
elif energy_cost >= 1 and energy_cost < 5:
    print("Cost category: Moderate cost")
else:
    print("Cost category: High cost")

#--------------------------------------------------------
#Question 2: Final Grade Calculator
#This program uses the data entered by the user (lab, midterm and final exam grades) to calculate and return to the user their final grade in that class taking into account each section's ponderation and classifies it by comparing it to a set grade.

#For the following lines, the user is prompted to type in the data needed (their grades) using their keyboards.
lab_grade = float(input("Enter the lab grade:"))
midterm_grade = float(input("Enter the midterm exam grade:"))
final_exam_grade = float(input("Enter the final exam grade:")) 


#In the lines below, a functuion is defined to calculate the final grade of a student, taking into account the grades they have entered into the program as well as their respective ponderation.
def calculate_grade(lab_grade, midterm_grade, final_exam_grade):
    final_grade = round((lab_grade * 0.30) + (midterm_grade * 0.30) + (final_exam_grade * 0.40), 1)
    return final_grade
 

#Here, the variable "final_grade" is defined and the student's final grade for that class is returned and displayed to them using the print function. 
final_grade = calculate_grade(lab_grade, midterm_grade, final_exam_grade)
print("Final grade:", final_grade) 

#In the lines below, the if/elif/else function is used to classify the student's grade as excellent, very good, good, satisfactory or as needs improvement by comparing it to a set grade and it returns the classification to the user following their final grade.
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
   
#-------------------------------------------------------
print("This is the end of the program!")
