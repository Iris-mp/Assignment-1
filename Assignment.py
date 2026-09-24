# -------------------------------------------------------
# Assignment 1
# Written by Iris-Maria Palade (2540435)
# For “Programming in Science” Section 00004 – Fall 2026
# --------------------------------------------------------
# #Question 1: Electricity Cost Calculator

power=int(input("Enter the power in watts:"))
time=int(input("Enter the number of hours:"))
rate=float(input("Enter the electricity rate per kWh:"))

def calculate_cost(power, time, rate):
    energy_cost=round((((power*time)/1000)*rate),2)
    return energy_cost
energy_cost=calculate_cost(power, time, rate)
print("Electricity cost:", calculate_cost(power, time, rate), "$")

if energy_cost<1:
    print("Cost category: Low cost")
elif energy_cost>1 and energy_cost<5:
    print("Cost category: Moderate cost")
else:
    print("Cost category: High cost")
# --------------------------------------------------------
# Question 2: Final Grade Calculator

lab_grade=int(input("Enter the lab grade:"))
midterm_grade=int(input("Enter the midterm exam grade:"))
final_exam_grade=int(input("Enter the final exam grade:"))

def calculate_grade(lab_grade, midterm_grade, final_grade):
    final_grade=round((lab_grade*0.30)+(midterm_grade*0.30)+(final_grade*0.40),1)
    return final_grade
final_grade=calculate_grade(lab_grade, midterm_grade, final_exam_grade)
print("Final grade:", final_grade)

if final_grade>=90:
    print("Result: Excellent")
elif final_grade>=80 and final_grade<90:
    print("Result: Very Good")
elif final_grade>=70 and final_grade<80:
    print("Result: Good")
elif final_grade>=60 and final_grade<70:
    print("Result: Satisfactory")
else:
    print("Result: Needs Improvement")
# -------------------------------------------------------