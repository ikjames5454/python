total_score = 0
number_of_student = 0
while True:
    individual_score = int(input("input score"))
    if individual_score == -25:
        break
    if individual_score > 0:
        total_score = total_score + individual_score
        number_of_student = number_of_student + 1
average_score = total_score / number_of_student
print("""******************************************************************
               Aso Rock Secondary School,Abuja Nigeria
******************************************************************
""")
print("Class:SSS 3", "\n")
print("Number of Student in Class:", number_of_student, "\n")
print("Total score:", total_score, "\n")
print("Average Score:", average_score, "\n")
print("******************************************************************")
