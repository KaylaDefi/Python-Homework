#-------------------------------------------
# Program Name: ITS320_CTA4_Option2.py
# Author: Kayla Sherwood
# Date: March 9, 2025
#-------------------------------------------
# Pseudocode:
# 1. Initialize an empty list to store grades.
# 2. Use a loop to prompt the user for five floating-point grades.
# 3. Store each entered grade in the list.
# 4. Calculate:
#    - Total sum of grades
#    - Average grade
#    - Maximum grade
#    - Minimum grade
# 5. Display the results.
#-------------------------------------------
# Program Inputs:
# - Five floating-point numbers representing student grades.
#-------------------------------------------
# Program Outputs:
# - The total sum of the grades.
# - The average grade.
# - The highest grade.
# - The lowest grade.
#-------------------------------------------


grades = []

for i in range(5):
    grade = float(input("Enter grade " + str(i + 1) + ": "))
    grades.append(grade)

average = sum(grades) / len(grades)  
maximum = max(grades)  
minimum = min(grades)  

print("\nGrade Statistics:")
print("Average Grade:", average)
print("Highest Grade:", maximum)
print("Lowest Grade:", minimum)
